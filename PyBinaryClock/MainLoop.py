__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import BinaryDisplay
from IO import IoInputs
import os

#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO
        self._gpio.setmode(self._gpio.BOARD)
        self._binDisplay = BinaryDisplay.BinaryDisplay()
        self._resetButton = IoInputs.PushButton(self._gpio,23)

    def initialize(self):
        print "Mainloop initialize"
        self._resetButton.initialize()
        self._binDisplay.initialize()
        self._binDisplay.test()
        #TODO: If network detected, update RTC

        self._lastUpdate = time.time()

    def update(self):
        btnstatus = self._resetButton.update()
        if btnstatus == "LongPressed":
            self._binDisplay.test()

        if time.localtime().tm_hour == 9 and time.localtime().tm_min < 10:
                self._binDisplay.showFikaPattern()
                print "Fika-tajm"
        else:
            if time.time() - self._lastUpdate > 0.1:
                self._lastUpdate = time.time()
                self._binDisplay.update()

    def __del__(self):
        self._gpio.cleanup()
        print "MainLoop cleaned up"


