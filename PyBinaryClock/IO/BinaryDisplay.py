__author__ = 'teddycool'
import time


TestArrayHrs= [1,0,1,1,1,1] # 10
TestArrayMin =[1,0,0,1,0,0,0] #37
TestArraySec =[0,1,1,0,1,1,0] #49


class BinaryDisplay(object):

    def __init__(self,gpio):
        print "Init BinaryDisplay object..."
        #lookup  for the binary column data
        self._figuredict ={0: [0,0,0,0],1:[1,0,0,0], 2: [0,1,0,0],3: [1,1,0,0] }
        self._ledstatusarray=[]

    #This methods sets the values for one column of the WS2812 leds
    def _setLeds(self, ledstatusarray ):
        print "_setLed started..."
        ledsetingarray = []

        return ledsetingarray

    #This method calulate the binary array for one column
    def _toBinary(self, value):
        print "_toBinary started..."

        valuearray = []

        return valuearray

    def setClock(self, time):
        print "_setLed started..."

        #Binary hrs, min and sec (6 columns) [2, 4, 3, 4, 3, 4]

        #Take values from array and set values for each position

        #Loop through all values to program the display-leds with the new setting, starting from 'end'
        #Bits shifted from the first led through the whole array


    def testBinaryDisplay(self, testtime):
        print "testClock started..."

        #Loop through all leds


    def update(self):
        self._ledstatusarray = []
        #Set current time...
        timestruct = time.localtime()
        #Hours...
        self._setLeds(self._figuredict[timestruct.tm_hours/10][:2]) #only first 2 in this column
        self._setLeds(self._figuredict[timestruct.tm_hours%10])
        #Minutes...







if __name__ == '__main__':
    import RPi.GPIO as GPIO
    print "Testcode for BinaryDisplay"
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)