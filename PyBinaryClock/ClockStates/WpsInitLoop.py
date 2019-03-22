from ClockStates import BaseStateLoop


class WpsInitLoop(BaseStateLoop.StateLoop):
    def __init__(self):
        super(BaseStateLoop, self).__init__()
        return


    def initialize(self):
        #Init WpsInitState
        return

    def update(self):
        #update WpsInitState
        #Check for new config now and then... or in mainloop?
        return