__author__ = 'teddycool'
import time
from neopixel import *

LED_COUNT = 20
LED_PIN = 18
LED_FREQ_HZ= 800000
LED_DMA= 10
LED_BRIGHTNESS= 100
LED_INVERT= False


class BinaryDisplay(object):

    def __init__(self):
        print "Init BinaryDisplay object..."
        #lookup  for the binary column data
        self._figuredict ={0: [0,0,0,0],1:[1,0,0,0], 2: [0,1,0,0],3: [1,1,0,0],
                            4: [0,0,1,0], 5:[1,0,1,0], 6:[0,1,1,0], 7: [1,1,1,0],
                            8: [0,0,0,1], 9: [1,0,0,1]}

        self._ledstatusarray=[]
        self._displayArray = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)


    def initialize(self):
        self._displayArray.begin()
        self._displayArray.setBrightness(50)


    #This methods sets the values for one column of the WS2812 leds
    def _setLeds(self, leds ):
        print leds
        self._ledstatusarray.extend(leds)



    def showFikaPattern(self):
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 50, 0, ))
        self._displayArray.show()
        time.sleep(2)
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
        self._displayArray.show()
        time.sleep(1)


    def test(self):
        print "testClock started..."

        #Loop through all leds
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
        self._displayArray.show()
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 50, 0, ))
            self._displayArray.show()
            time.sleep(0.1)
        time.sleep(2)
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(50, 0, 0, ))
            self._displayArray.show()
            time.sleep(0.1)
        time.sleep(2)
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
            self._displayArray.show()
            time.sleep(0.1)


    def update(self):
        self._ledstatusarray = []
        #Set current time...
        timestruct = time.localtime()
        print  timestruct

        #Start from the rigth since firs led (index 0) is the lowest rightmost led
        self._setLeds(self._figuredict[timestruct.tm_sec % 10])
        self._setLeds(self._figuredict[timestruct.tm_sec / 10][:3])  # only first 3 figuredict in this column
        self._setLeds(self._figuredict[timestruct.tm_min % 10])
        self._setLeds(self._figuredict[timestruct.tm_min / 10][:3])  # only first 3 figuredict in this column
        self._setLeds(self._figuredict[timestruct.tm_hour % 10])
        self._setLeds(self._figuredict[timestruct.tm_hour / 10][:2])  # only first 2 figuredict in this column

        #Set the values of each pixel
        for led in range(0, len(self._ledstatusarray), 1):
            if self._ledstatusarray[led] == 0:
                self._displayArray.setPixelColor(led,Color(0, 7, 0)) #Color when 'off'
            else:
                self._displayArray.setPixelColor(led, Color(80, 0, 0,)) #Color when 'on'

        #Turn them on with new values
        self._displayArray.show()


    def off(self):
        #Turn off the display...
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
        self._displayArray.show()



if __name__ == '__main__':
  #  import RPi.GPIO as GPIO
    print "Testcode for BinaryDisplay"
   # import RPi.GPIO as GPIO
    #GPIO.setmode(GPIO.BOARD)
    bd= BinaryDisplay()
    bd.initialize()
    bd.test()
    while(1):
        bd.update()
        time.sleep(0.1)
