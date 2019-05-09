from ClockStates import BaseStateLoop
from Connectivity import WiFi
import os
import time


class WpsInitLoop(BaseStateLoop.StateLoop):
    def __init__(self):
        super(WpsInitLoop, self).__init__()
        return


    def initialize(self):
        #Init WpsInitState
        self._wifi = WiFi.WiFi()
        return

    def update(self, context):
        if self._wifi.WpsConnectStart(context):
            print "Press WPS on router"
            if self._wifi.WpsConnectionCheck(context):
                print "Connected"
                # TODO: move handling of HW clock to RTC class..
                time.sleep(5)
                print "Will update HW clock..."
                print "System time: " + time.asctime(time.localtime())
                os.system('sudo hwclock -s')
                context._setState("ClockLoop")
            else:
                print "WPS Connection FAILED"
                context._setState("ClockInit")
        else:
            print "WPS PBC FAILED"
            context._setState("ClockInit")
        return