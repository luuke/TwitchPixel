import json
from enum import Enum

class MessageType(Enum):
    UNKNOWN = -1
    PONG = 0
    RECONNECT = 1
    MESSAGE = 2
    MESSAGE_REWARD_REDEEMED = 3

class Message:
    _json = str()
    _dict = dict()
    Type = MessageType.UNKNOWN

class PubSubParser:
    @staticmethod
    def parse(msgJson: str):
        msg = Message()
        msg._json = msgJson
        msg._dict = json.loads(msg._json)
        print("parse():", msg._dict)

        if "type" in msg._dict:
            msg.Type = msg._dict["type"]
            if((msg.Type == "PONG") or 
               (msg.Type == "RECONNECT")):
                return msg


