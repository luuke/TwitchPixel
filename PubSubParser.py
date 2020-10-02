from enum import Enum

class MessageType(Enum):
    PONG = 0
    RECONNECT = 1
    MESSAGE = 2
    MESSAGE_REWARD_REDEEMED = 3

class Message:
    def __init__(self, type: MessageType):
        self.type = type
