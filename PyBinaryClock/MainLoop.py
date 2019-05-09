__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import BinaryDisplay
from IO import IoInputs
from IO import TempMonitor
from IO import LightSensor
import os
from ClockStates import ClockInit
from ClockStates import ClockLoop
from ClockStates import WpsInitLoop
from ClockStates import NoTimeState


#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO
        self._gpio.setmode(self._gpio.BCM)
        self._binDisplay = BinaryDisplay.BinaryDisplay()
        self._s1 = IoInputs.PushButton(self._gpio, 11)  #S1: WiFi-setup
        self._s2 = IoInputs.PushButton(self._gpio, 9)   #S2:
        self._s3 = IoInputs.PushButton(self._gpio, 10)  #S3:
        self._tm = TempMonitor.TempMonitor()
        self._ls = LightSensor.LightSensor(self._gpio,14)
        self._states = {"ClockInit": ClockInit.ClockInit(), "ClockLoop": ClockLoop.ClockLoop(),
                        "WpsInit": WpsInitLoop.WpsInitLoop(),"NoValidTime": NoTimeState.NoTimeState()}

    def initialize(self):
        print "Mainloop initialize"
        self._s1.initialize()
        self._binDisplay.initialize()
        self._tm.initialize()
        self._binDisplay.SetBrightness(60)
        self._ls.initialize()

        self._lastUpdate = time.time()
        self._lastTempCheck = time.time()
        self._lastLightCheck=time.time()
        for state in self._states:
            self._states[state].initialize()
        self._setState("ClockInit")

    def update(self):
        #Logic for all states:

        # #Check if wifi button pressed


        #Check background ligth and set brigthness... normal 50, min 30 and max 80...
        ligth = int(self._ls.update())
        if ligth > 0:
            if ligth > 5:
                brightn = 40
            elif ligth < 3:
                brightn = 100
            else:
                brightn = 60
            self._binDisplay.SetBrightness(brightn)

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
        print "Switching state to : " + newstate
        self._myState=self._states[newstate]

    def __del__(self):
        self._binDisplay.off()
        self._gpio.cleanup()
        print "MainLoop cleaned up"

