import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')

from bridgeclient import BridgeClient as bridgeclient

if __name__ == '__main__':

    _client=bridgeclient()
    while True:
	print _client.get('key')
