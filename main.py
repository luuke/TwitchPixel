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
import json
import re
from LedStrip import LedStrip
from PubSubClient import PubSubClient

twitchWebsocketsUrl = 'wss://pubsub-edge.twitch.tv'
ledStrip = LedStrip(10)

def setLed(r=0, g=0, b=0):
    print("Setting RGB: " + r,g,b)
    ledStrip.setColor((r,g,b))

with open('.env', 'r') as secretsFile:
    secretsJson = json.load(secretsFile)
    accessToken = secretsJson['AccessToken']

async def main():
    while True:
        msg = await pubsub.getNextMessage()
        print("main(): " + msg)
        try:
            msg = json.loads(msg)["data"]["message"]
            msg = json.loads(msg)["data"]["redemption"]["user_input"]
            colors = msg.split()
            print("main(): " + str(colors))
            setLed(int(colors[0]),int(colors[1]),int(colors[2]))
        except Exception as e:
            print("Exception:", e)

if __name__ == "__main__":
    pubsub = PubSubClient(accessToken, ["channel-points-channel-v1.56618017"])
    asyncio.get_event_loop().run_until_complete(pubsub.connect())

    tasks = [
        asyncio.ensure_future(pubsub.receive()),
        asyncio.ensure_future(pubsub.heartbeat()),
        asyncio.ensure_future(main())
    ]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
