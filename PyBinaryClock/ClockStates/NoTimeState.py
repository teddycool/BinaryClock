from ClockStates import BaseStateLoop
import time

class NoTimeState(BaseStateLoop.StateLoop):
    def __init__(self):
        super(NoTimeState, self).__init__()
        return


    def initialize(self):
        #Init clockstate
        print "NoTimeState initialize"
        return

    def update(self, context):
        context._binDisplay.showNoValidTimePattern()

        s1status = context._s1.update()
        if s1status == "LongPressed":
            context._setState("WpsInit")
