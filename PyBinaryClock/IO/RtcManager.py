__author__ = 'teddycool'

# check once in a while if internet is available and the update systemtime and rtc

class RtcManager(object):

    def __init__(self,gpio):
        print "Init RtcManager object..."