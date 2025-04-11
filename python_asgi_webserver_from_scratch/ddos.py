import asyncio
import socket
 
HTTP_REQUEST = b'GET /foo HTTP/1.1\r\nHost: localhost:8000\r\nUser-Agent: python/3.10.12\r\nAccept: */*\r\n\r\n'
 
HOST = '127.0.0.1'    # The remote host
PORT = 8000              # The same port as used by the server

async def send_request():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    writer.write(HTTP_REQUEST)
    await writer.drain()
    
    data = await reader.read(1024)
    writer.close()
    await writer.wait_closed()
    
    print('Received', repr(data))
    return data

# This is how the traditional socket approach would look:
async def send_request_with_socket():
    # This would block the event loop without special handling
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)  # Need to manually set non-blocking
    
    # Would need to await loop.sock_connect() instead of direct connect
    await asyncio.get_event_loop().sock_connect(sock, (HOST, PORT))
    await asyncio.get_event_loop().sock_sendall(sock, HTTP_REQUEST)
    data = await asyncio.get_event_loop().sock_recv(sock, 1024)
    sock.close()
    
    print('Received', repr(data))
    return data

async def main():
    # Create 500 tasks to run concurrently
    tasks = (send_request_with_socket() for _ in range(500))
    
    # Run all tasks concurrently and wait for them to complete
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    asyncio.run(main())