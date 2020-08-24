import websocket

class PubSubClient:
    def __init__(self, accessToken, topics):
        self._url = 'wss://pubsub-edge.twitch.tv' 
        self._topics = topics
        self._accessToken = accessToken
        self._connection = websocket.WebSocket()

    def connect(self):
        self._connection.connect(self._url)
        msg='{"type":"LISTEN", "nonce":"1234554321", "data": {"topics": ["channel-points-channel-v1.56618017"], "auth_token": "' + self._accessToken + '"}}'
        self._connection.send(msg)

    def receive(self):
        return self._connection.recv()
    