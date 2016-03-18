import env
import variable
import threading
import logging

def waitAndExecuteCommand(commandChannel):
    print "wait"
    while True:
        command = commandChannel.recv(1024)
        logging.info("recv:" + command)
        # command can be a response of heart beat or an update of the LED_control,
        # so we split by ',' and drop device id and device key and check length
        fields = command.split(',')[2:]

        if len(fields) > 1:
            timeStamp, dataChannelId, commandString = fields
            #if dataChannelId == 'led_control':
                # check the value - it's either 0 or 1
            #    commandValue = int(commandString)
            #    logging.info("led :%d" % commandValue)
            #    setLED(commandValue)

def rawInputTest(channel):
    x = raw_input(">>> Input: ")
    env.sendCommand(channel, "mtardirf", x);
    print x

if __name__ == '__main__':
    #setupLED()
    channel = env.establishCommandChannel()
    t = threading.Timer(1, waitAndExecuteCommand, [channel]);
    t.start()
    #t = threading.Thread(name='wait', target=waitAndExecuteCommand(channel))
    #t.setDaemon(true)
    #t.start();
    #waitAndExecuteCommand(channel)
    while (True):
        rawInputTest(channel)
