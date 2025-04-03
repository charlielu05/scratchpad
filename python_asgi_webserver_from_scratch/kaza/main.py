import asyncio
from kaza.server import Server
import importlib

class NoAppFoundError(Exception):
    pass


def get_from_str(input_str):
    module_str, attrs_str = input_str.split(":")
    try:
        module = importlib.import_module(module_str)
        app = getattr(module, attrs_str)
        return app
    except ModuleNotFoundError as exc:
        raise NoAppFoundError()


def main():
    from application import app
    server = Server(app, '127.0.0.1', 8000)
    asyncio.run(server.start())

if __name__ == "__main__":
    main()