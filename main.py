print("TwitchPixel!")

import board
import neopixel
import websocket
import json

twitchWebsocketsUrl = 'wss://pubsub-edge.twitch.tv'

with open('.env', 'r') as secretsFile:
    secretsJson = json.load(secretsFile)
    accessToken = secretsJson['AccessToken']

ws = websocket.create_connection(twitchWebsocketsUrl)
msg='{"type":"LISTEN", "nonce":"1234554321", "data": {"topics": ["channel-points-channel-v1.56618017"], "auth_token": "' + accessToken + '"}}'
ws.send(msg)

print(ws.recv())

pixels = neopixel.NeoPixel(board.D18, 10)

while True:
    rcv = ws.recv()
    msg = json.loads(json.loads(rcv)["data"]["message"])
    input = msg["data"]["redemption"]["user_input"]
    input = input.split()

    for j in range(9):
        pixels[j] = (int(input[0]),int(input[1]),int(input[2]))

    pixels.show()