import asyncio
from kaza.server import Server

def main():
    from application import app
    server = Server(app, '127.0.0.1', 8000)
    asyncio.run(server.start())

if __name__ == "__main__":
    main()