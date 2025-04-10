import socket
import asyncio

HTTP_REQUEST = b'GET /foo HTTP/1.1\r\nHost: localhost:8000\r\nUser-Agent: python/3.10.12\r\nAccept: */*\r\n\r\n'

HOST = '127.0.0.1'    # The remote host
PORT = 8000              # The same port as used by the server

async def send_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(HTTP_REQUEST)
        data = s.recv(1024)
    
    print('Received', repr(data))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    
    ddos_tasks = (await send_request() for _ in range(500))
    
    loop.run_until_complete(ddos_tasks)