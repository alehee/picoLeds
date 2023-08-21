from networking import Networking
from controller import Controller
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

        endpoint = request.split()[1]
        response = "No endpoint found"
        
        if endpoint.startswith('/color/'):
            color = endpoint.removeprefix('/color/')
            response = controller.changeColor(color)

        elif endpoint.startswith('/brightness/'):
            brightness = endpoint.removeprefix('/brightness/')
            response = controller.changeBrightness(brightness)

        if response == 'OK':
            cl.send(f'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n')
        else:
            cl.send(f'HTTP/1.1 400 Bad Request\r\nContent-type: text/html\r\n\r\n')

        cl.send(response)
        cl.close()
    except Exception as e:
        pass
