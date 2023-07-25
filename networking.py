import network
import socket
from time import sleep

class Networking:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.ip = None

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        self.ip = wlan.ifconfig()[0]
        print(f'Connected on {self.ip} with hostname {network.hostname()}')
        return self.ip
