from application import app
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost", required=False, dest="host")
    parser.add_argument("--port", type=int, default=20001, required=False, dest="port")
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)
