from ClockStates import BaseStateLoop
from ClockStates import WpsInitLoop
import time



class ClockLoop(BaseStateLoop.StateLoop):
    def __init__(self):
        super(ClockLoop, self).__init__()
        return


    def initialize(self):
        #Init clockstate
        print "ClockLoop initialize"
        return

    def update(self, context):
        #update clockloop
        #Check lightsensor and adjust brightness
        #Check if fika-tajm
        #Check if alarm-time or any other time related events
        #Time-states?

        if time.time() - context._lastUpdate > 0.2:
            context._lastUpdate = time.time()
            context._binDisplay.update()
        btnstatus = context._resetButton.update()
        if btnstatus == "LongPressed":
            context._binDisplay.test()

        # if time.localtime().tm_hour == 9 and (time.localtime().tm_min > 10 and time.localtime().tm_min < 20):
        #     self._binDisplay.showFikaPattern()
        #     print "Fika-tajm"
        #
        # if time.localtime().tm_hour == 14 and (time.localtime().tm_min > 30 and time.localtime().tm_min < 40):
        #     self._binDisplay.showFikaPattern()
        #     print "Fika-tajm"
        return