from networking import Networking
from controller import Controller
from endpoint import Endpoint
import json

config = json.load(open('config.json'))

print('Initializing leds')
ledsConfig = config['leds']
controller = Controller(ledsConfig['count'], ledsConfig['pin'])

print('Initializing network')
networkConfig = config['network']
network = Networking(networkConfig['networkSsid'], networkConfig['networkPassword'], networkConfig['hostedPort'])
network.connect()

print('Opening socket')
network.socket_open()
network.updateIpAddress(networkConfig['endpointUrl'], config['id'])

print('Running loop')
while True:
    try:
        cl, addr = network.socket.accept()
        request = str(cl.recv(1024))
        request = request.split()[1]
        head, response = Endpoint.validate(request, controller)
        cl.send(head)
        cl.send(json.dumps(response))
        cl.close()
    except KeyboardInterrupt:
        network.socket.close()
