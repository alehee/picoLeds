from led import Led

class Controller:
    def __init__(self, count, port):
        self.leds = []
        self.count = count
        self.port = port
        self.isOn = False
        self.brightness = 50
        self.initialize()

    def initialize(self):
        for i in range(0, self.count):
            self.leds.append(Led('#C00000'))

    def changeColor(self, color):
        # TODO
        print(f'Changed color to {color}')
        return 'OK'

    def changeBrightness(self, brightness):
        self.brightness = brightness
        # TODO
        print(f'Changed brightness to {brightness}')
        return 'OK'
