__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import BinaryDisplay
from IO import IoInputs
from IO import TempMonitor
from IO import LightSensor
import os

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
#        self._ls.initialize()
        self._binDisplay.SetBrightness(50)
        #self._binDisplay.test()
        #TODO: If network detected, update RTC

        self._lastUpdate = time.time()
        self._lastTempCheck = time.time()
        self._lastLightCheck=time.time()

    def update(self):
        btnstatus = self._resetButton.update()
        if btnstatus  == "Pressed":
            self._binDisplay.ToggleBrightness()
        if btnstatus == "LongPressed":
            self._binDisplay.test()

        # if time.localtime().tm_hour == 9 and (time.localtime().tm_min > 10 and time.localtime().tm_min < 20):
        #     self._binDisplay.showFikaPattern()
        #     print "Fika-tajm"
        #
        # if time.localtime().tm_hour == 14 and (time.localtime().tm_min > 30 and time.localtime().tm_min < 40):
        #     self._binDisplay.showFikaPattern()
        #     print "Fika-tajm"
        #
        if time.time() - self._lastUpdate > 0.1:
            self._lastUpdate = time.time()
            self._binDisplay.update()
        #     cnt = self._ls.update()
        #     if cnt > 0:
        #         self._lightindex = cnt  #Update current ligthindex if needed
        #
        # if time.time()-self._lastLightCheck > 10:
        #     if self._lightindex > 4:
        #         self._binDisplay.SetBrightness(20)
        #     elif self._lightindex ==  3:
        #         self._binDisplay.SetBrightness(50)
        #     else:
        #         self._binDisplay.SetBrightness(70)
        #     self._lastLightCheck=time.time()

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


    def __del__(self):
        self._binDisplay.off()
        self._gpio.cleanup()
        print "MainLoop cleaned up"


