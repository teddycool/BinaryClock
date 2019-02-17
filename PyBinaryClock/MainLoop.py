__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import BinaryDisplay
from IO import IoInputs
from IO import TempMonitor
import os

#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO
        self._gpio.setmode(self._gpio.BOARD)
        self._binDisplay = BinaryDisplay.BinaryDisplay()
        self._resetButton = IoInputs.PushButton(self._gpio,23)
        self._tm = TempMonitor.TempMonitor()

    def initialize(self):
        print "Mainloop initialize"
        self._resetButton.initialize()
        self._binDisplay.initialize()
        self._tm.initialize()
        self._binDisplay.test()
        #TODO: If network detected, update RTC

        self._lastUpdate = time.time()
        self._lastTempCheck = time.time()

    def update(self):
        btnstatus = self._resetButton.update()
        if btnstatus == "LongPressed":
            self._binDisplay.test()

        if time.localtime().tm_hour == 9 and time.localtime().tm_min < 15:
            self._binDisplay.showFikaPattern()
            print "Fika-tajm"

        if time.localtime().tm_hour == 14 and (time.localtime().tm_min > 30 and time.localtime().tm_min < 45):
            self._binDisplay.showFikaPattern()
            print "Fika-tajm"

        if time.time() - self._lastUpdate > 0.1:
               self._lastUpdate = time.time()
               self._binDisplay.update()


        if time.time() - self._lastTempCheck > 10:
            if self._tm.get_cpu_temperature() > 50:
                print "High temp!"
                print "Shutting down..."
                os.system('sudo shutdown -h now')


    def __del__(self):
        self._binDisplay.off()
        self._gpio.cleanup()
        print "MainLoop cleaned up"


