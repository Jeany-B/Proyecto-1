#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

def mover_adelante():

    tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 2)

    return