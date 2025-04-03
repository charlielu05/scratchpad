import asyncio
import socket

class Http_Parse_Error(Exception):
    pass

def serialize_http_response(asgi_responses):
        http_response = b""
        headers = {}

        for response in asgi_responses:
            response_type = response.get("type")

            if response_type == "http.response.start":
                status_code = response.get("status", 200)
                http_response += f"HTTP/1.1 {status_code} OK\r\n".encode()

                for header in response.get("headers", []):
                    key, value = header
                    headers[key] = value

            elif response_type == "http.response.body":
                http_response += b"\r\n".join(
                    [f"{key.decode()}: {value.decode()}".encode() for key, value in headers.items()])
                http_response += b"\r\n\r\n" + response.get("body", b"")

        return http_response
    
class Request:
    def __init__(self):
        self.request = {}
    
    def parse_http(self,payload:bytes)->str:
        try:
            request, headers_body = payload.split(b'\r\n', 1)
            self.request['method'], self.request['path'], self.request['type_version'] = request.split(b' ')
            
            *headers, body = headers_body.split(b'\r\n')
            self.request['type'], self.request['http_version'] = self.request.get('type_version').split(b'/')
            # unpack the headers array into list of dict
            headers_array = []
            for header in filter(lambda x: x != b'', headers):
                key, val = header.split(b':', 1)
                headers_array.append((key.strip(), val.strip()))
                
            self.request['headers'] = headers_array
        except:
            return Http_Parse_Error
        
class ASGI:
    def __init__(self, request:Request):
        self.scope:dict = {
            'asgi': {
                'version': '3.0',
                'spec_version': '2.0'
            },
            'method': request.request['method'].decode(),
            'type': request.request['type'].decode().lower(),
            'http_version': request.request['http_version'].decode(),
            'path': request.request['path'].decode(),
            'headers': request.request['headers'],
            'query_string': b'',
        }
        self.response = []
        self.response_event = asyncio.Event()
    
    async def run(self, app):
        await app(self.scope, self.receive, self.send)
    
    async def send(self, message):
        self.response.append(message)
        if message.get('type') == "http.response.body":
            self.response_event.set()
    
    async def receive(self):
        message = {
            "type": "http.request",
            "body": self.request.get('body',None),
            "more_body": False,
        }
        return message
     
class ConnectionHandler:
    def __init__(self, connection, loop, app):
        self.connection = connection
        self.loop = loop
        self.app = app

    async def handle_connection(self):
        try:
            data = await self.loop.sock_recv(self.connection, 1024)
            request_object:Request = Request()
            request_object.parse_http(data)
            asgi = ASGI(request_object)
            print(asgi.scope)
            asyncio.create_task(asgi.run(self.app))
            await asgi.response_event.wait()
            http_response = serialize_http_response(asgi.response)
            print(f"http_response: {http_response}")
            await self.loop.sock_sendall(self.connection, http_response)

        except Exception as e:
            print(f"exception:{e}")
        except Http_Parse_Error as e:
            print("Http parser exception...", e)
        finally:
            self.connection.close()
            
class Server:
    def __init__(self, app, host, port):
        self.app = app
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setblocking(False)
        self.server_socket.bind((self.host, self.port))

    async def listen_for_connections(self, loop):
        self.server_socket.listen()
        print(f"Listening on {self.host, self.port}")
        while True:
            connection, address = await loop.sock_accept(self.server_socket)
            print(f"{address} connected")
            connection_handler = ConnectionHandler(connection, loop, self.app)
            asyncio.create_task(connection_handler.handle_connection())


    async def start(self):
        loop = asyncio.get_event_loop()
        await self.listen_for_connections(loop)

if __name__ == "__main__":
    server = Server('127.0.0.1', 8000)
    asyncio.run(server.start())