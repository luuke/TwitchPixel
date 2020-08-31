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

        if IsRaspberryPi == true:
            pixels = neopixel.NeoPixel(board.D18, self._length)
        else
            pixels = None