__author__ = 'teddycool'
#http://stackoverflow.com/questions/17304225/how-to-detect-if-computer-is-contacted-to-the-internet-with-python
#Handle check of internetconnection and turning on/off a indication led
import os
import time
import urllib2


class InternetDetection(object):

    def __init__(self):
        print "Init"
        self._lastCheck = 0 #Force check at first update
        self._connected = "Not connected"


    def initialize(self):
        print "Initialize"


    def update(self):
        self._connected = "Not connected"
        if time.time() - self._lastCheck > 10:
            try:
                urllib2.urlopen("http://www.google.com").close()
                self._connected = "Connected"
            except:
                pass
        return self._connected


if __name__ == '__main__':
    print "Testcode for NetDetector"
    nd = InternetDetection()
    nd.initialize()
    while(True):
        print nd.update()
        time.sleep(1)