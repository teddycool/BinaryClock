# BinaryClock
A project to create a binary clock with a specially designed circuit-board and a raspberrypi zero

This project contains of two parts:
The circuitboard, made in Eagle CAD and the Raspberrypi code, python 2.7 written in PyCharm Community edition.

The circuit board is a 'hat' to a raspberry pi zero with 20 WS2812B programmable LEDs for the clock-display, a 2x20 header
for the pi connection and a connection for a DS3231 RTC. The board was manufactured by https://aisler.net that has a great quality service for small series of prototypes. 

 See pictures below for one type of assembly with plexiglass as a 'sandwich'.

The code depend on https://github.com/rpi-ws281x/rpi-ws281x-python Install this first.

It is a very simple 'game-loop' kind of program that updates every 1/10 second. Taking current time and  split to each figure (collumn) and then calculate  the bit-pattern and set the LEDs accordingly.
A simple user-manual and a technical description can be found in the project directory..

Future sw-improvements will add possibillities to configure colors and brightnessetc from outside.

Hardware version 3 is now ready and added a real-time clock directly on the circuitboard, some IOs to be controled by time, some extra buttons and a circuit for measuring the background light. 

Ref1: https://en.wikipedia.org/wiki/Binary_clock
Ref2: https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/


Pictures of hw version 1:
<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191029.jpg" alt="Front..."/>

<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191040.jpg" alt="Rear..."/>

<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191052.jpg" alt="Side..."/>

