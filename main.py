from networking import Networking
import json

config = json.load(open('config.json'))

print('Initializing network')
networkConfig = config['network']
network = Networking(networkConfig['networkSsid'], networkConfig['networkPassword'])
network.connect()