#!/usr/bin/env python3

from time import sleep

#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
#from ev3dev2.sensor import INPUT_1
#from ev3dev2.sensor.lego import TouchSensor
#from ev3dev2.led import Leds
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

TANK_DRIVE = MoveTank(OUTPUT_A, OUTPUT_B)

MOTOR_IZQUIERDO = LargeMotor(OUTPUT_A)
MOTOR_DERECHO = LargeMotor(OUTPUT_B)
#MOTOR_APRETAR_GARRA = MediumMotor(OUTPUT_C)
#MOTOR_SUBIR_BAJAR = LargeMotor(OUTPUT_D)

# GARRA = LargeMotor(OUTPUT_C)
RAPIDO = SpeedPercent(100)
MEDIO = SpeedPercent(50)
LENTO = SpeedPercent(10)

def avanzar():
    TANK_DRIVE.on_for_seconds(-50, -50, 1)

def retroceder():
    TANK_DRIVE.on_for_seconds(50, 50, 1)

def girar_derecha():
    TANK_DRIVE.on_for_seconds(-50, 50, 1)

def girar_izquierda():
    TANK_DRIVE.on_for_seconds(50, -50, 1)
    

def hablar():
    sound = Sound()
    sound.speak("Hello")
