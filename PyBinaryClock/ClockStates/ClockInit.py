from ClockStates import BaseStateLoop
import urllib2


class ClockInit(BaseStateLoop.StateLoop):
    def __init__(self):
        super(ClockInit, self).__init__()
        return


    def initialize(self):
        #Init clockinit state
        print "ClockInit initialize"
        return

    def update(self, context):
        #TODO: check for network and time status
        try:
            urllib2.urlopen("http://www.google.com").close()
            connected = True
            print "Connected"
        except:
            connected = False
            print "NOT Connected"

        if connected:
            context._setState("ClockLoop")
        else:
            # TODO: fix a clock set state...
            #TODO: Check if there is some valid time to read from RTC, if not ?
            context._setState("WpsInit")

