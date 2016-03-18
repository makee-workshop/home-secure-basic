import variable
import video

def rawInputTest():
    x = raw_input(">>> Input: ")
    print x
    if x=='1':
        video.enableVideo()
    else:
        video.disableVideo()

if __name__ == '__main__':

    while (True):
        rawInputTest()
