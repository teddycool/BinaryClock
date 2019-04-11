__author__ = 'teddycool'
#REF: http://www.rpiblog.com/2012/11/reading-analog-values-from-digital-pins.html
#This is calibrated with a LDR GL  5516 and a 47uF elotrolytic capacitor.

import time

class LightSensor(object):

    def __init__(self,gpio,pin=14):
        self._gpio=gpio
        self._pin = pin


    def initialize(self):
        # Discharge capacitor
        self._gpio.setup(self._pin, self._gpio.OUT)
        self._gpio.output(self._pin, self._gpio.LOW)
        time.sleep(0.1)
        self._lastDischarge = time.time()
        time.sleep(0.1)
        self._gpio.setup(self._pin, self._gpio.IN)


    def update(self):
        if self._gpio.input(self._pin) == self._gpio.LOW:   #still LOW, continue to count time...
            return 0.0
        else:
            dtime = time.time()-self._lastDischarge
            self.initialize()
            return dtime

if __name__ == '__main__':
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    print "Testcode for LightSensor"
    ls=LightSensor(GPIO, 14)
    ls.initialize()
    while True:
        print ls.update()
        time.sleep(0.1)







