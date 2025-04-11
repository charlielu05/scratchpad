import socket

HTTP_REQUEST = b'GET / HTTP/1.1\r\nHost: localhost:8000\r\nUser-Agent: python/3.10.12\r\nAccept: */*\r\n\r\n'

HOST = '127.0.0.1'    # The remote host
PORT = 8000              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(HTTP_REQUEST)
    data = s.recv(1024)
    
print('Received', repr(data))