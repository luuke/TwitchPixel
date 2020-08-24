import json
import websocket

class PubSubClient:
    def __init__(self, accessToken, topics):
        self._url = 'wss://pubsub-edge.twitch.tv' 
        self._topics = topics
        self._accessToken = accessToken
        self._connection = websocket.WebSocket()

    def connect(self):
        msg='{"type":"LISTEN", "nonce":"1234554321", "data": {"topics": ["channel-points-channel-v1.56618017"], "auth_token": "' + self._accessToken + '"}}'
        self._connection.connect(self._url)
        self._connection.send(msg)
        print("Connection status:" + self._connection.recv()) # TODO: Replace with connection success/fail handling

    def receive(self):
        msg = self._connection.recv()
        return json.loads(msg)["data"]["message"]
    