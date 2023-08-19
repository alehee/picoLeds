import network
import socket
import urequests as requests
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
    
    def updateIpAddress(self, url, id):
        call = f'{url}?id={id}&ip={self.ip}'
        print(f'Call to endpoint `{call}`')
        request = requests.get(call)
        print(f'Request result: {request.content}')
        
