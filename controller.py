from neopixel import Neopixel

class Controller:
    def __init__(self, count, pin):
        self.strip = None
        self.count = count
        self.pin = pin
        self.isOn = True
        self.color = (0, 80, 0)
        self.brightness = 50
        self.initialize()

    def initialize(self):
        self.strip = Neopixel(self.count, 0, self.pin, "GRB")
        self.updateLeds()

    def changeColor(self, color):
        try:
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            if rgb[0] < 0 or rgb[0]>255 or rgb[1] < 0 or rgb[1]>255 or rgb[2] < 0 or rgb[2]>255:
                raise Exception("Color not valid")
            self.color = rgb
            self.updateLeds()
            print(f'Changed color to {rgb}')
            return 'OK'
        except Exception as e:
            print(e)
            return 'Color changing failed'

    def changeBrightness(self, brightness):
        try:
            brightness = int(brightness)
            if brightness < 0 or brightness > 255:
                raise Exception("Brightness range not valid")
            self.brightness = brightness
            self.updateLeds()
            print(f'Changed brightness to {brightness}')
            return 'OK'
        except Exception as e:
            print(e)
            return e
        
    def toggleLeds(self, isOn):
        try:
            self.isOn = isOn
            self.updateLeds()
            print(f'Changed powering to {isOn}')
            return 'OK'
        except Exception as e:
            print(e)
            return e
        
    def updateLeds(self):
        if self.isOn:
            self.strip.fill(self.color)
        else:
            self.strip.fill((0,0,0))
        self.strip.brightness(self.brightness)
        self.strip.show()
