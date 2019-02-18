# BinaryClock
A project to create a binary clock with a specially designed circuit-board and a raspberrypi zero

This project contains of two parts:
The circuitboard and the raspberrypi code in python 2.7

The circuit board is a sort of 'hat' to a raspberry pi zero with 20 WS2812B programmable LEDs for the clock-display, a 2x20 header
for the pi connection and a connection for a DS3231 RTC.

The kit is mounted between two part of plexi-glass panels to make a clock that can be mounted on the wall. See pictures below.

The code depend on AdaFruit_NeoPixel:  pip install rpi_ws281x

It is a very simple 'game-loop' kind of program that updates every 1/10 second. Taking current time and  split to each figure (collumn) and then calculate  the bit-pattern and set the LEDs accordingly.

Future sw-improvements will be a possibillity to configure colors and brightness from outside, maybe a BT interface or a 'webpage' kind of thing...

Future hw-improvemnts will be added to make it possible to have some IOs controled by time. In version 1 the connection to the RTC didn't work correctly and this will also be fixed.

Ref1: https://en.wikipedia.org/wiki/Binary_clock
Ref2: https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/


<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191029.jpg" alt="Front..."/>

<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191040.jpg" alt="Rear..."/>

<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191052.jpg" alt="Side..."/>

