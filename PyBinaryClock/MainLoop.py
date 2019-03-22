__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import BinaryDisplay
from IO import IoInputs
from IO import TempMonitor
from IO import LightSensor
import os
#from ClockStates import ClockLoop
from ClockStates import ClockInit


#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO
        self._gpio.setmode(self._gpio.BCM)
        self._binDisplay = BinaryDisplay.BinaryDisplay()
        self._resetButton = IoInputs.PushButton(self._gpio,11)
        self._tm = TempMonitor.TempMonitor()
#        self._ls=LightSensor.LightSensor(self._gpio,14)

    def initialize(self):
        print "Mainloop initialize"
        self._resetButton.initialize()
        self._binDisplay.initialize()
        self._tm.initialize()
        self._binDisplay.SetBrightness(50)

        self._lastUpdate = time.time()
        self._lastTempCheck = time.time()
        self._lastLightCheck=time.time()
        self._setState(ClockInit.ClockInit())
       # self._myState.initialize()

    def update(self):
        # Check for new config now and then... or in mainloop?
        #TODO: move last time update to clock-loop
        if time.time() - self._lastTempCheck > 10:
            temp = self._tm.get_cpu_temperature()
            self._lastTempCheck=time.time()
            print "CPU-temp: " + str(temp)
            if self._tm.get_cpu_temperature() > 60:
                self._binDisplay.off()
                print "High temp!"
                print "Shutting down..."
                f = file(time.asctime() + "temp.log", 'w')
                f.write("High temperature!")
                f.write(str(temp))
                f.close()
                time.sleep(5)
                os.system('sudo shutdown -h now')

        self._myState.update(self)


    def _setState(self, newstate):
        print "Switching state to : " + str(newstate)
        self._myState=newstate

    def __del__(self):
        self._binDisplay.off()
        self._gpio.cleanup()
        print "MainLoop cleaned up"


