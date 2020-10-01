import asyncio
import json
import websockets
import queue

class PubSubClient:
    def __init__(self, accessToken, topics):
        self._url = 'wss://pubsub-edge.twitch.tv' 
        self._topics = topics
        self._accessToken = accessToken
        self._messages = queue.Queue()

    async def connect(self):
        msg='{"type":"LISTEN", "nonce":"1234554321", "data": {"topics": ["channel-points-channel-v1.56618017"], "auth_token": "' + self._accessToken + '"}}'
        self._connection = await websockets.client.connect(self._url)
        await self._connection.send(msg)
        print("Connection status:" + await self._connection.recv()) # TODO: Replace with connection success/fail handling

    async def receive(self):
        while True:
            print("receive()")
            msg = await self._connection.recv()
            self._messages.put(msg)

    async def heartbeat(self):
        while True:
            print("heartbeat()")
            if self._connection.open:
                print("heartbeat(): Connection opened")
            await asyncio.sleep(5)

    async def getNextMessage(self):
        while True:
            try:
                print("getNextMessage()")
                return self._messages.get_nowait()
            except queue.Empty:
                print("getNextMessage(): sleep")
                await asyncio.sleep(1)    