import websockets
import asyncio
from paths import SOCKET_URL
from credentials import Credentials as cr
from json import dumps


class AvanzaSocket:
    def __init__(self) -> None:
        self.url
        self.cookie
        self.credentials
        self.socket

    async def handShake(self) -> None:
        message = {
            'test': 'test'
        }
        await self.send(message)

    async def initConnection(self) -> None:
        self.url = SOCKET_URL
        self.cookie = cr.loadCookie()
        async with websockets.connect(self.url, extra_headers={self.cookie}) as self.socket:
            await self.handShake

    async def send(self, message) -> dict:
        self.socket.send(dumps(message))
        response = self.socket.recv()
        return response
