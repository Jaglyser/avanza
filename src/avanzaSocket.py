import asyncio
from login import Login as ln
from paths import constants, SOCKET_URL
import websockets


class Socket:
    def __init__(self) -> None:
        self.cookie = ln.getCookie()
        self.socket = None
        self.connectionStatus = False

    async def setup(self) -> None:
        asyncio.ensure_future(self.createSocket())
        await self.connectSocket()

    async def createSocket(self) -> None:
        async with websockets.connect(SOCKET_URL, extra_headers={self.cookie}) as self.socket:
            await self.socketMessage

    async def connectSocket():
        timeout_count = 40
        timeout_value = 0.250

        for _ in range(0, timeout_count):
            if self._connected:
                return
            await asyncio.sleep(timeout_value)

        raise TimeoutError('\
            We weren\'t able to connect \
            to the websocket within the expected timeframe \
        ')

    async def socketMessage(self):
        await self.__send({
            'advice': {
                'timeout': 60000,
                'interval': 0
            },
            'channel': '/meta/handshake',
            'ext': {'subscriptionId': self._push_subscription_id},
            'minimumVersion': '1.0',
            'supportedConnectionTypes': [
                'websocket',
                'long-polling',
                'callback-polling'
            ],
            'version': '1.0'
        })


socket = Socket()
await socket.createSocket()
