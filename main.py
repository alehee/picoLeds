from networking import Networking
import json

config = json.load(open('config.json'))
network = Networking(config['networkSsid'], config['networkPassword'])