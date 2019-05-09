from ClockStates import BaseStateLoop
import urllib2
import os
import time


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
            # TODO: move handling of HW clock to RTC class..
            print "Will update HW clock..."
            print "System time: " + time.asctime(time.localtime())
           # print "Your time zone is set to UTC : " + str(time.timezone)
            time.sleep(5)
            os.system('sudo hwclock -s')
            context._setState("ClockLoop")
        else:
            #TODO: fix a clock set state...
            #TODO: Check if there is some valid time to read from RTC, if not ?
            #TODO: move handling of HW clock to RTC class..
            # TODO: move handling of HW clock to RTC class..
            print "System time is set to: " + time.asctime(time.localtime())
            timeres = os.popen('sudo hwclock -r').read()
            if time.localtime().tm_year >= 2019:
                context._setState("ClockLoop")
            else:
                context._setState("NoValidTime")
                print "System time is ruled as not set correctly. Try to connect to a network"