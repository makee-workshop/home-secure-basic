import requests
import socket
import threading
import logging
import variable
# change this to the values from MCS web console

# change 'INFO' to 'WARNING' to filter info messages
logging.basicConfig(level='INFO')

heartBeatTask = None

def establishCommandChannel():
    # Query command server's IP & port
    connectionAPI = 'https://api.mediatek.com/mcs/v2/devices/%(device_id)s/connections.csv'
    r = requests.get(connectionAPI % variable.DEVICE_INFO,
                 headers = {'deviceKey' : variable.DEVICE_INFO['device_key'],
                            'Content-Type' : 'text/csv'})
    logging.info("Command Channel IP,port=" + r.text)
    (ip, port) = r.text.split(',')

    # Connect to command server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    s.settimeout(None)

    # Heartbeat for command server to keep the channel alive
    def sendHeartBeat(commandChannel):
        keepAliveMessage = '%(device_id)s,%(device_key)s,0' % variable.DEVICE_INFO
        commandChannel.sendall(keepAliveMessage)
        logging.info("beat:%s" % keepAliveMessage)

    def heartBeat(commandChannel):
        sendHeartBeat(commandChannel)
        # Re-start the timer periodically
        global heartBeatTask
        heartBeatTask = threading.Timer(40, heartBeat, [commandChannel]).start()

    heartBeat(s)
    return s

def sendCommand(commandChannel, channelId, value):
    deviceId = variable.DEVICE_INFO['device_id']
    deviceKey = variable.DEVICE_INFO['device_key']
    keepAliveMessage = '%s,,%s' % (channelId, value)
    url = "https://api.mediatek.com/mcs/v2/devices/%s/datapoints.csv" % deviceId
    requests.post(url, data=keepAliveMessage, headers={'deviceKey' : deviceKey,'Content-Type' : 'text/csv'})

