import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')

from bridgeclient import BridgeClient as bridgeclient

if __name__ == '__main__':
    try:
        raw = sys.argv[1]
    except IndexError as e1:
        raw = raw_input('>>> Input (0 or 1) : ')

    _client = bridgeclient()
    _client.put('key', raw)
    print _client.get('key')
