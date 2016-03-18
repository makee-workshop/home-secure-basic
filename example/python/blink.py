import requests
import socket
import threading
import logging
import subprocess
import video
#import mraa
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
    #print deviceId
    keepAliveMessage = '%s,,%s' % (channelId, value)
    commandChannel.sendall(keepAliveMessage)
    logging.info("beat:%s" % keepAliveMessage)
    #setValueAPI = 'https://api.mediatek.com/mcs/v2/devices/%(device_id)s/connections.csv'
    #r = requests.get(connectionAPI % variable.DEVICE_INFO,
    #             headers = {'deviceKey' : variable.DEVICE_INFO['device_key'],
    #                        'Content-Type' : 'text/csv'})
    url = "https://api.mediatek.com/mcs/v2/devices/Dn7nTI0I/datapoints.csv"
    requests.post(url, data=keepAliveMessage, headers={'deviceKey' : deviceKey,'Content-Type' : 'text/csv'})



def waitAndExecuteCommand(commandChannel):
    p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
    	print line,
    retval = p.wait()

    while True:
        command = commandChannel.recv(1024)
        logging.info("recv:" + command)
        # command can be a response of heart beat or an update of the LED_control,
        # so we split by ',' and drop device id and device key and check length
        fields = command.split(',')[2:]

        if len(fields) > 1:
            timeStamp, dataChannelId, commandString = fields
            if dataChannelId == 'led_control':
                # check the value - it's either 0 or 1
                commandValue = int(commandString)
                logging.info("led :%d" % commandValue)
                #setLED(commandValue)

#pin = None
#def setupLED():
    global pin
    # on LinkIt Smart 7699, pin 44 is the Wi-Fi LED.
    #pin = mraa.Gpio(44)
    #pin.dir(mraa.DIR_OUT)

#def setLED(state):
    # Note the LED is "reversed" to the pin's GPIO status.
    # So we reverse it here.
    #if state:
        #pin.write(0)
    #else:
        #pin.write(1)
def rawInputTest(channel):
    x = raw_input(">>> Input: ")
    sendCommand(channel, "mtardirf", x);
    print x

if __name__ == '__main__':
    #setupLED()
    video.enableVideo();
    channel = establishCommandChannel()
    t = threading.Timer(1, waitAndExecuteCommand, [channel]);
    t.start()
    #t = threading.Thread(name='wait', target=waitAndExecuteCommand(channel))
    #t.setDaemon(true)
    #t.start();
    #waitAndExecuteCommand(channel)
    while (True):
        rawInputTest(channel)


