try:
    import board
    import neopixel
    IsRaspberryPi = True
    print('Application running on Raspberry Pi')
except (ImportError, NotImplementedError):
    IsRaspberryPi = False
    print('Application running on PC')

class LedStrip:
    def __init__(self, length=1):
        self._length = length

        if IsRaspberryPi == True:
            pixels = neopixel.NeoPixel(board.D18, self._length)
        else:
            pixels = None

    def setColor(self, rgb=(0,0,0)):
        print("setColor(): " + str(rgb))
        for j in range(9):
            pixels[j] = (min(abs(rgb[0]),255), min(abs(rgb[1]),255), min(abs(rgb[2]),255))
        pixels.show()

