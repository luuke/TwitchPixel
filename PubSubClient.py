import asyncio
import json
import websockets

class PubSubClient:
    def __init__(self, accessToken, topics):
        self._url = 'wss://pubsub-edge.twitch.tv' 
        self._topics = topics
        self._accessToken = accessToken

    async def connect(self):
        msg='{"type":"LISTEN", "nonce":"1234554321", "data": {"topics": ["channel-points-channel-v1.56618017"], "auth_token": "' + self._accessToken + '"}}'
        self._connection = await websockets.client.connect(self._url)
        await self._connection.send(msg)
        print("Connection status:" + await self._connection.recv()) # TODO: Replace with connection success/fail handling

    async def receive(self):
        while True:
            print("test")
            msg = await self._connection.recv()
            print(msg)
            # return json.loads(msg)["data"]["message"]

    async def heartbeat(self):
        while True:
            print("heartbeat")
            if self._connection.open:
                print("Open")
            await asyncio.sleep(5)

    