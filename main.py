print("TwitchPixel!")

import board
import neopixel
import websocket
import json

twitchWebsocketsUrl = 'wss://pubsub-edge.twitch.tv'

secretsFile = open('.env', 'r')
secrets = secretsFile.readlines()
accessToken = secrets[0][:-1] # :-1 to get rid of new line at the end of secret

ws = websocket.create_connection(twitchWebsocketsUrl)
msg='{"type":"LISTEN", "nonce":"1234554321", "data": {"topics": ["channel-points-channel-v1.56618017"], "auth_token": "' + accessToken + '"}}'
ws.send(msg)

print(ws.recv())

pixels = neopixel.NeoPixel(board.D18, 10)

# for i in range(1):
while True:
    rcv = ws.recv()
    msg = json.loads(json.loads(rcv)["data"]["message"])
    input = msg["data"]["redemption"]["user_input"]
    input = input.split()

    for j in range(9):
        pixels[j] = (int(input[0]),int(input[1]),int(input[2]))

    pixels.show()
