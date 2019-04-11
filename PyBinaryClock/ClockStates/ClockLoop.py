from ClockStates import BaseStateLoop
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

        if time.time() - context._lastUpdate > 0.2:
            context._lastUpdate = time.time()
            context._binDisplay.update()

        s1status = context._s1.update()
        if s1status == "LongPressed":
            context._setState("WpsInit")

