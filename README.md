# BinaryClock
A project to create a binary clock with a specially designed circuit-board and a raspberrypi zero

This project contains of several parts:
    * The circuitboard, made in Eagle CAD 
    * Raspberrypi code in python 2.7 written in PyCharm Community edition.
    * 3d models for a 3d-printed to the enclosure, made with tinkercad

Assembled and mounted in the 3d-printed enclosure:


The circuit board is a 'hat' to a raspberry pi zero with 20 WS2812B programmable LEDs for the clock-display, a 2x20 header
for the pi connection and some extra IOs and buttons. The board was manufactured by https://aisler.net that has a great quality service for small series of prototypes. 

The code depend on https://github.com/rpi-ws281x/rpi-ws281x-python Install this first.

It is a very simple 'game-loop' kind of program that updates every 1/5 second. Taking current time and  split to each figure (collumn) and then calculate  the bit-pattern and set the LEDs accordingly.

A simple user-manual and a technical description can be found in the project directory..

Future sw-improvements will add possibillities to configure colors and brightnes etc from outside.

Hardware version 3 is now ready and added a real-time clock directly on the circuitboard, some IOs to be controled by time, some extra buttons and a circuit for measuring the background light. 

Future hw-improvements will be to move the buttons to a better position when using the enclosure. 

Ref1: https://en.wikipedia.org/wiki/Binary_clock
Ref2: https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/

See pictures below for an other type of assembly with plexiglass as a 'sandwich'.

Pictures of hw version 1:
<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191029.jpg" alt="Front..."/>

<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191040.jpg" alt="Rear..."/>

<img src="https://github.com/teddycool/BinaryClock/blob/master/20190218_191052.jpg" alt="Side..."/>

