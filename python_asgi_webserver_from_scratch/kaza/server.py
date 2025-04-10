import asyncio
import socket
from dataclasses import dataclass

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
    
@dataclass
class Request:
    method: bytes = None
    path: bytes = None
    type: bytes = None
    type_version: bytes = None
    http_version: bytes = None 
    headers: bytes = None
    body: bytes = None
    
def parse_http(payload:bytes)->Request:
    try:
        request, headers_body = payload.split(b'\r\n', 1)
        method, path, type_version = request.split(b' ')    
        *headers, body = headers_body.split(b'\r\n')
        request_type,  http_vesrion = type_version.split(b'/')
        
        # unpack the headers array into list of dict
        headers_array = []
        for header in filter(lambda x: x != b'', headers):
            key, val = header.split(b':', 1)
            headers_array.append((key.strip(), val.strip()))

        return Request(method=method, path=path, type=request_type, 
                                 type_version=type_version, http_version=http_vesrion,
                                 headers=headers_array, body=body)
    
    except Exception as e:
        raise Http_Parse_Error(f"error parsing http request: {e}")
        
class ASGI:
    # reference to uvicorn's implementation: https://github.com/encode/uvicorn/blob/4fdfec4adf1ba6da5e65c8422321e203b6050052/uvicorn/protocols/http/httptools_impl.py#L435
    def __init__(self, request:Request):
        self.scope:dict = {
            'asgi': {
                'version': '3.0',
                'spec_version': '2.0'
            },
            'method': request.method.decode(),
            'type': request.type.decode().lower(),
            'http_version': request.http_version.decode(),
            'path': request.path.decode(),
            'headers': request.headers,
            'query_string': b'',
        }
        self.body:bytes = request.body
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
            "body": self.body,
            "more_body": False,
        }
        return message
            
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
            asyncio.create_task(self.handle_connection(connection, loop, self.app))

    async def start(self):
        loop = asyncio.get_event_loop()
        await self.listen_for_connections(loop)
        
    async def handle_connection(self, connection, loop, app):
        try:
            data = await loop.sock_recv(connection, 1024)
            print(f"\n data received: {data} \n")

            request_object = parse_http(data)
            print(f"\n request_object:{request_object} \n")
            
            asgi = ASGI(request_object)
            print(f"\n asgi.scope:{asgi.scope} \n")
            
            asyncio.create_task(asgi.run(app))
            await asgi.response_event.wait()
            print(f"\n asgi.response: {asgi.response} \n")
            http_response = serialize_http_response(asgi.response)
            print(f"\n http_response: {http_response} \n")
            await loop.sock_sendall(connection, http_response)

        except Exception as e:
            print(f"exception:{e}")
        except Http_Parse_Error as e:
            print("Http parser exception...", e)
        finally:
            connection.close()


if __name__ == "__main__":
    server = Server('127.0.0.1', 8000)
    asyncio.run(server.start())