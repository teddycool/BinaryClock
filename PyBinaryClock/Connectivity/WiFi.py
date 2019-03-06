__author__ = 'teddycool'
#REF: https://w1.fi/cgit/hostap/plain/wpa_supplicant/README-WPS

import os

class WiFi(object):

    def __init(self):
        print "Init WiFi management"


    def WpsConnectStart(self):
        wpsresult = os.system('sudo wpa_cli wps_pbc') #try to use wps push button mode

        if wpsresult.contains('p2p'):  #zero default p2p for wlan is set, this must be removed
            os.system('sudo rm /var/run/wpa_supplicant/p2p-dev-wlan0')
            wpsresult = os.system('sudo wpa_cli wps_pbc')  # try to use wps push button mode

        return  wpsresult.contains('wlan0')


    def update(self):
        #Statemachine to handle wifi connection...





