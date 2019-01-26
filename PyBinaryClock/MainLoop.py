__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import BinaryDisplay

#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO
        self._gpio.setmode(self._gpio.BOARD)
        self._binDisplay = BinaryDisplay.BinaryDisplay(self._gpio)

    def initialize(self):
        print "Mainloop initialize"
        self._binDisplay.testBinaryDisplay(2)
        #TODO: If network detected, update RTC

        self._lastUpdate = time.time()

    def update(self):

        if time.time() - self._lastUpdate > 1:
            self._lastUpdate = time.time()
            #TODO: update the display...

    def __del__(self):
        self._gpio.cleanup()
        print "MainLoop cleaned up"


