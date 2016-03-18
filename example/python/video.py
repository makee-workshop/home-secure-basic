import subprocess
import variable

def enableVideo():
    deviceId = variable.DEVICE_INFO['device_id']
    deviceKey = variable.DEVICE_INFO['device_key']
    dataChannelId =  variable.DEVICE_INFO['video_channel_id']
    width = 176;
    height = 144;

    cmd = 'ffmpeg -s %dx%d -f video4linux2 -r 30 -i /dev/video0 -f mpeg1video -r 30 -b 800k http://stream-mcs.mediatek.com/%s/%s/%s/%d/%d' % (width, height, deviceId, deviceKey, dataChannelId, width, height)
    print cmd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

def disableVideo():
    print 'disable'
    p = subprocess.Popen('killall ffmpeg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()
