__author__ = 'teddycool'

# check once in a while if internet is available and the update systemtime and rtc
#REF: https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/,

>>> import os, time
>>> time.strftime('%X %x %Z')
'12:45:20 08/19/09 CDT'
>>> os.environ['TZ'] = 'Europe/London'
>>> time.tzset()
>>> time.strftime('%X %x %Z')
'18:45:39 08/19/09 BST'

from IO import ntplib
from time import ctime
c = i.NTPClient()
response = c.request('pool.ntp.org')
print(ctime(response.tx_time))


class RtcManager(object):

    def __init__(self,gpio):
        print "Init RtcManager object..."