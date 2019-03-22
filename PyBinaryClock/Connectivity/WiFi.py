__author__ = 'teddycool'
#REF: https://w1.fi/cgit/hostap/plain/wpa_supplicant/README-WPS
#https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python

import os
import urllib2
import time

class WiFi(object):

    def __init(self):
        print "Init WiFi management"


    def WpsConnectStart(self):
        print "WiFi connection start"
        wpsresult = os.system('sudo wpa_cli wps_pbc') #try to use wps push button mode

        if wpsresult.contains('p2p'):  #zero default p2p for wlan is set, this must be removed
            os.system('sudo rm /var/run/wpa_supplicant/p2p-dev-wlan0')
            wpsresult = os.system('sudo wpa_cli wps_pbc')  # try to use wps push button mode
        return  wpsresult.contains('wlan0')


    def WpsConnectionCheck(self):
        print " Checking connection...."
        while True:
            for i in range(120):
                try:
                    urllib2.urlopen("http://www.google.com").close()
                    return True
                except:
                    pass
                time.sleep(1)
            return False


  #  def resetwifi(self):
        # Rewrite an empty wpa_supplicant.conf and reboot...



if __name__ == '__main__':
  #  import RPi.GPIO as GPIO
    print "Testcode for WiFi"
    wifi=WiFi()
    if wifi.WpsConnectStart():
        print "Press WPS on  router"
        if wifi.WpsConnectionCheck():
            print "Connected"
        else:
            print "WPS Connection FAILED"
    else:
        print "WPS PBC FAILED"
