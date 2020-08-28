print("TwitchPixel!")

try:
    import board
    import neopixel
    IsRaspberryPi = True
    print('Application running on Raspberry Pi')
except (ImportError, NotImplementedError):
    IsRaspberryPi = False
    print('Application running on PC')

import websocket
import json
from PubSubClient import PubSubClient

twitchWebsocketsUrl = 'wss://pubsub-edge.twitch.tv'

def setLed(r=0, g=0, b=0):
    print(r,g,b)
    
    if IsRaspberryPi == True:
        pixels = neopixel.NeoPixel(board.D18, 10)
        
        for j in range(9):
            pixels[j] = (r,g,b)
        pixels.show()


with open('.env', 'r') as secretsFile:
    secretsJson = json.load(secretsFile)
    accessToken = secretsJson['AccessToken']

pubsub = PubSubClient(accessToken, ["channel-points-channel-v1.56618017"])
pubsub.connect()


while True:
    rcv = pubsub.receive()
    msg = json.loads(rcv)
    
    msgType = msg["type"]
    redemptionTitle = msg["data"]["redemption"]["reward"]["title"]

    if msgType != "reward-redeemed":
        print("Invalid message type")
        print(msgType)
        continue

    if redemptionTitle != "[In development] Control LEDs":
        print("Invalid redemption type")
        continue

    input = msg["data"]["redemption"]["user_input"]
    input = input.split()

    setLed(int(input[0]),int(input[1]),int(input[2]))