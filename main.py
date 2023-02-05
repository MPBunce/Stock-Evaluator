import asyncio
import websockets
import json

from datetime import datetime
from tabulate import tabulate
from decimal import Decimal


ticker = input("Please enter the ticker of stock you want to evaluate: ")

print(ticker)

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


asyncio.run(hello())