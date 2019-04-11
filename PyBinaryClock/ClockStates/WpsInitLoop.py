from ClockStates import BaseStateLoop
from Connectivity import WiFi



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
            print "Press WPS on  router"
            if self._wifi.WpsConnectionCheck(context):
                print "Connected"
                #TODO: set HW clock
                context._setState("ClockLoop")
            else:
                print "WPS Connection FAILED"
                context._setState("ClockLoop")
        else:
            print "WPS PBC FAILED"
        return