from networking import Networking
import json

config = json.load(open('config.json'))
networkConfig = config['network'];
network = Networking(networkConfig['networkSsid'], networkConfig['networkPassword'])