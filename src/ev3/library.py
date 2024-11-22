#!/usr/bin/env python3

from time import sleep

from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor, MoveJoystick
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

TANK_DRIVE = MoveTank(OUTPUT_A, OUTPUT_B)
#TANK_CLAW = MoveTank(OUTPUT_C, OUTPUT_D)
JOYSTICK_DRIVE = MoveJoystick(OUTPUT_A, OUTPUT_B)

MOTOR_IZQUIERDO = LargeMotor(OUTPUT_A)
MOTOR_DERECHO = LargeMotor(OUTPUT_B)
MOTOR_SUBIR_BAJAR = MediumMotor(OUTPUT_C)
MOTOR_APRETAR_GARRA = MediumMotor(OUTPUT_D)

RAPIDO = SpeedPercent(100)
MEDIO = SpeedPercent(50)
LENTO = SpeedPercent(10)

def frenar():
    TANK_DRIVE.on(0, 0)

def movimiento_joystick(x, y):
    # Deadzone
    if (x >= 0.1 and y >= 0.1):
        JOYSTICK_DRIVE.on(x, y)
    else:
        JOYSTICK_DRIVE.on(0, 0)

def avanzar():
    # TANK_DRIVE.on_for_seconds(-50, -50, 1)
    TANK_DRIVE.on(-50, -50)

def retroceder():
    TANK_DRIVE.on(50, 50)
    #TANK_DRIVE.on_for_seconds(50, 50, 1)

def girar_derecha():
    TANK_DRIVE.on(50, -50)
    #TANK_DRIVE.on_for_seconds(-50, 50, 1)

def girar_izquierda():
    TANK_DRIVE.on(-50, 50)
    #TANK_DRIVE.on_for_seconds(50, -50, 1)

def parar_garra():
    MOTOR_SUBIR_BAJAR.on(0,0)
    MOTOR_APRETAR_GARRA.on(0,0)


def subir_garra():
    print(MOTOR_SUBIR_BAJAR.position())
    #MOTOR_SUBIR_BAJAR.on_for_seconds(-40, 1)

def bajar_garra():
    MOTOR_SUBIR_BAJAR.on_for_seconds(40, 1)

def abrir_garra():
    MOTOR_APRETAR_GARRA.on_for_seconds(10, 0.5)
    
def cerrar_garra():
    MOTOR_APRETAR_GARRA.on_for_seconds(-10, 0.5)

def hablar():
    sound = Sound()
    sound.speak("Hello")
