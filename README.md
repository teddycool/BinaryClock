# BinaryClock
A project to create a binary clock with a home-made circuit-board and a raspberrypi zero

This project contains of two parts:
The circuitboard and the raspberrypi code in python 2.7

The circuit board is a sort of 'hat' to a raspberry pi zero with 20 WS2813B programmable LEDs for the clock-display, a 2x20 header
for the pi connection and a connection for a DS3231 RTC.

I aim to mount this on the back-side of a plexi-glass panel to make a clock that can be mounted on the wall. Pictures and drawings of this 
will also be published when ready.

The code depend on AdaFruit_NeoPixel:  pip install rpi_ws281x

Ref1: https://en.wikipedia.org/wiki/Binary_clock
Ref2: https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/
