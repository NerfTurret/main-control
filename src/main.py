import sys
import asyncio
import websockets
from constants import *


async def main():
    async with websockets.connect(f"{WS_URL}{CONN_ID}") as ws:
        while True:
            try:
                msg = await ws.recv()
                print(msg)
            except websockets.exceptions.ConnectionClosed:
                print("Connection with server closed")
                break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        CONN_ID = int(sys.argv[1])
    asyncio.get_event_loop().run_until_complete(main())
    