print("TwitchPixel!")

import board
import neopixel
import websocket
import json
from PubSubClient import PubSubClient

twitchWebsocketsUrl = 'wss://pubsub-edge.twitch.tv'

with open('.env', 'r') as secretsFile:
    secretsJson = json.load(secretsFile)
    accessToken = secretsJson['AccessToken']

pubsub = PubSubClient(accessToken, ["channel-points-channel-v1.56618017"])
pubsub.connect()

pixels = neopixel.NeoPixel(board.D18, 10)

while True:
    rcv = pubsub.receive()
    msg = json.loads(rcv)
    input = msg["data"]["redemption"]["user_input"]
    input = input.split()

    for j in range(9):
        pixels[j] = (int(input[0]),int(input[1]),int(input[2]))

    pixels.show()