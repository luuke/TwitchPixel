print("TwitchPixel!")

try:
    import board
    import neopixel
    IsRaspberryPi = True
    pixels = neopixel.NeoPixel(board.D18, 10)
    print('Application running on Raspberry Pi')
except (ImportError, NotImplementedError):
    IsRaspberryPi = False
    print('Application running on PC')

import asyncio
# import websocket
import json
import re
from PubSubClient import PubSubClient

twitchWebsocketsUrl = 'wss://pubsub-edge.twitch.tv'

def setLed(r=0, g=0, b=0):
    print(r,g,b)
    print(min(abs(r),255), min(abs(g),255), min(abs(b),255))
    
    if IsRaspberryPi == True:
        for j in range(9):
            pixels[j] = (min(abs(r),255), min(abs(g),255), min(abs(b),255))
        pixels.show()


with open('.env', 'r') as secretsFile:
    secretsJson = json.load(secretsFile)
    accessToken = secretsJson['AccessToken']

# pubsub = PubSubClient(accessToken, ["channel-points-channel-v1.56618017"])
# pubsub.connect()

if __name__ == "__main__":
    pubsub = PubSubClient(accessToken, ["channel-points-channel-v1.56618017"])
    asyncio.get_event_loop().run_until_complete(pubsub.connect())
    
    tasks = [
        asyncio.ensure_future(pubsub.test()),
        asyncio.ensure_future(pubsub.heartbeat())
    ]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

# while True:

    
#     rcv = pubsub.receive()
#     pubsub.heartbeat()

#     msg = json.loads(rcv)
    
#     msgType = msg["type"]
#     redemptionTitle = msg["data"]["redemption"]["reward"]["title"]

#     if msgType != "reward-redeemed":
#         print("Invalid message type")
#         print(msgType)
#         continue

#     if redemptionTitle != "[In development] Control LEDs":
#         print("Invalid redemption type")
#         continue

#     userInput = msg["data"]["redemption"]["user_input"]

#     rgb = re.search("[0-9]+ [0-9]+ [0-9]+", userInput)

#     if rgb is None:
#         print("Invalid user input: " + userInput)
#     else:
#         print("User input: " + userInput)
#         colors = rgb[0].split()
#         setLed(int(colors[0]),int(colors[1]),int(colors[2]))