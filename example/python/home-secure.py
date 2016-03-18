import variable
import env
import video

import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')

from bridgeclient import BridgeClient as bridgeclient

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


def sendCommand(commandChannel, channelId, value): 
    deviceId = variable.DEVICE_INFO['device_id']                                
    deviceKey = variable.DEVICE_INFO['device_key']                              
    keepAliveMessage = '%s,,%s' % (channelId, value)                            
    commandChannel.sendall(keepAliveMessage)                                    
    logging.info("beat:%s" % keepAliveMessage)  
    url = "https://api.mediatek.com/mcs/v2/devices/%s/datapoints.csv" %(deviceId)                                              
    requests.post(url, data=keepAliveMessage, headers={'deviceKey' : deviceKey,'Content-Type' : 'text/csv'}) 

def yunbridge:
    _client=bridgeclient()
    while True:
        rf = _client.get('rf')
        if rf=='1':
	    sendCommand(channel, "mtardirf", 1);
            print 1
        else :
            sendCommand(channel, "mtardirf", 0);
            print 0

def rawInputTest(channel):                                                      
    x = raw_input(">>> Input: ")                                                
    sendCommand(channel, "back_led", x);                                        
    print x 

if __name__ == '__main__':
    channel = establishCommandChannel()
    
    t1 = threading.Timer(1, waitAndExecuteCommand, [channel]);                   
    t1.start() 

    t2 = threading.Timer(1, yunbridge, []);                   
    t2.start() 
    
    while (True):                                                               
        rawInputTest(channel)
