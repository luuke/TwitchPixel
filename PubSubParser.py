from enum import Enum

class MessageType(Enum):
    PONG = 0
    RECONNECT = 1
    MESSAGE = 2
    MESSAGE_REWARD_REDEEMED = 3

