__author__ = 'teddycool'
#REF: https://w1.fi/cgit/hostap/plain/wpa_supplicant/README-WPS
#https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python

import os
import urllib2
import time

class WiFi(object):

    def __init(self):
        print "Init WiFi management"


    def WpsConnectStart(self, context):
        print "WiFi connection start"
        context._binDisplay.showWiFiConnectionStart()
        wpsresult = os.popen('sudo wpa_cli wps_pbc').read() #try to use wps push button mode
        print wpsresult
        if wpsresult.find('p2p') == -1:
            return True

        if wpsresult.find('p2p') > -1 :  #zero default p2p for wlan is set, this must be removed
            os.system('sudo rm /var/run/wpa_supplicant/p2p-dev-wlan0')
            wpsresult = os.popen('sudo wpa_cli wps_pbc').read()  # try to use wps push button mode
            if wpsresult.find('p2p') == -1 :
                return True
            else:
                return False

    def WpsConnectionCheck(self, context):
        print " Checking connection...."
        connected = context._binDisplay.showWiFiConnectionProgress()
        return connected



  #  def resetwifi(self):
        # Rewrite an empty wpa_supplicant.conf and reboot...



if __name__ == '__main__':
    import RPi.GPIO as GPIO
    import MainLoop
    context = MainLoop.MainLoop()
    context.initialize()

    print "Testcode for WiFi"
    wifi=WiFi()
    if wifi.WpsConnectStart():
        print "Press WPS on  router"
        if wifi.WpsConnectionCheck(context):
            print "Connected"
        else:
            print "WPS Connection FAILED"
    else:
        print "WPS PBC FAILED"
