import network
import urequests as requests
import socket
from time import sleep

class Networking:
    def __init__(self, ssid, password, port):
        self.ssid = ssid
        self.password = password
        self.ip = None
        self.port = port
        self.socket = socket.socket()

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
        print(f'Request result: {request.text}')

    def socket_open(self):
        addr = (self.ip, self.port)
        self.socket.bind(addr)
        self.socket.listen(1)
        print(f'Listening to {addr}')

    
