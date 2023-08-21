from networking import Networking
from controller import Controller
from endpoint import Endpoint
import json

config = json.load(open('config.json'))

print('Initializing leds')
ledsConfig = config['leds']
controller = Controller(ledsConfig['count'], ledsConfig['port'])

print('Initializing network')
networkConfig = config['network']
network = Networking(networkConfig['networkSsid'], networkConfig['networkPassword'], networkConfig['hostedPort'])
network.connect()

print('Opening socket')
network.socket_open()
network.updateIpAddress(networkConfig['endpointUrl'], config['id'])

while True:
    try:
        cl, addr = network.socket.accept()
        print('client connected from', addr)
        request = str(cl.recv(1024))
        print(request)

        validation = Endpoint.validate(request)
        print(validation)

        if validation[0] == 200:
            print(f'Changing to {validation[2]}')

        cl.send(f'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(validation[1])
        cl.close()
    except Exception as e:
        pass
