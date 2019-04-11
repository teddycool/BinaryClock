__author__ = 'teddycool'

#https://github.com/rpi-ws281x/rpi-ws281x-python

import time
from rpi_ws281x import *
import urllib2

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
        self._brightness = 50


    def showFikaPattern(self):
        time.sleep(1)
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(0, 50, 0, ))
        self._displayArray.show()
        time.sleep(1)

    def showWiFiConnectionStart(self):
        time.sleep(1)
        for i in range(20):
            self._displayArray.setPixelColor(i, Color(50, 50, 0, ))
        self._displayArray.show()
        time.sleep(1)
        self.off()

    def showWiFiConnectionProgress(self ):
        connected = False
        while not connected:
            for i in range(20):
                try:
                    print "Trying to connect..."
                    self._displayArray.setPixelColor(i, Color(0, 50, 0, ))
                    self._displayArray.show()
                    urllib2.urlopen("http://www.google.com").close()
                    connected = True
                    time.sleep(6)
                    break
                except:
                    self._displayArray.setPixelColor(i, Color(0, 0, 50, ))
                    self._displayArray.show()
                time.sleep(6)
        self.off()
        return connected




    def test(self):
        print "Test started..."

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


    def SetBrightness(self, brightness):
        if self._brightness == brightness:
            pass
        else:
            self._brightness= brightness
            self._displayArray.setBrightness(brightness)
            print "New brightness: " + str(brightness)


    def update(self):
        self._ledstatusarray = []
        #Set current time...
        timestruct = time.localtime()
        #print  timestruct

        #Start from the rigth since first led (index 0) is the lowest rightmost led
        self._ledstatusarray.extend((self._figuredict[timestruct.tm_sec % 10]))
        self._ledstatusarray.extend((self._figuredict[timestruct.tm_sec / 10][:3]))  # only first 3 figuredict in this column
        self._ledstatusarray.extend((self._figuredict[timestruct.tm_min % 10]))
        self._ledstatusarray.extend((self._figuredict[timestruct.tm_min / 10][:3]))  # only first 3 figuredict in this column
        self._ledstatusarray.extend((self._figuredict[timestruct.tm_hour % 10]))
        self._ledstatusarray.extend((self._figuredict[timestruct.tm_hour / 10][:2]))  # only first 2 figuredict in this column

        #Set the values of each pixel
        for led in range(0, len(self._ledstatusarray), 1):
            if self._ledstatusarray[led] == 0:
                self._displayArray.setPixelColor(led,Color(8, 0, 0)) #Color when 'off'
            else:
                self._displayArray.setPixelColor(led, Color(0, 50, 0,)) #Color when 'on'

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
    bd.off()
    bd.showWiFiConnectionProgress()
    while(1):
        bd.update()
        time.sleep(0.1)


