import variable
import requests
import env
import video
import threading
import logging
import time
import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')

from bridgeclient import BridgeClient as bridgeclient

grf = '0'

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

def yunbridge():
    global grf                                                                                              
    _client=bridgeclient()                                                                                  
    while True:                   
	time.sleep( 1 )                                                                              
        rf = _client.get('rf')                                                                              
        if rf=='1':                                                                                         
            if grf=='0':                                                                                    
                sendCommand(channel, "mtardirf", 1);                                                        
                grf = '1'                                                                                   
                print 1                                                                                     
        elif rf=='0':                                                                                       
            if grf=='1':                                                                                    
                sendCommand(channel, "mtardirf", 0);                                                        
                grf='0'                                                                                     
                print 0            

def rawInputTest(channel):                                                      
    x = raw_input(">>> Input: ")                                                
    sendCommand(channel, "back_led", x);                                        
    print x 

if __name__ == '__main__':
    channel = env.establishCommandChannel()
    
    t1 = threading.Timer(1, waitAndExecuteCommand, [channel]);                   
    t1.start() 

    t2 = threading.Timer(1, yunbridge, []);                   
    t2.start() 
    
    while (True):                                                               
        rawInputTest(channel)
