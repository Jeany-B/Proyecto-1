#!/usr/bin/env python3
# encoding=utf-8

import socket
import library as lib

HOST = ""
PORT = 8080

# Creación y setup de socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket creado")
    s.bind((HOST, PORT))
    print("El socket se creo con puerto: " + str(PORT))
    s.listen(4)
    print("El socket esta escuchando...")

    # Se espera la conexión con el cliente
    client, addr = s.accept()
    print("Se conecto a " + str(addr))

    # Main loop
    while True:
        # Se recibe un byte y se decodifica
        data = client.recv(16)
        key = data.decode()

        print(key)
        #Movimiento
        if key == 'w-presionada':
            lib.avanzar()

        elif key == "w-soltada":
            lib.frenar()

        elif key == 'a-presionada':
            lib.girar_izquierda()
            print("a")

        elif key == 'a-soltada':
            lib.frenar()
            print("a")

        elif key == 's-presionada':
            lib.retroceder()
            print("s")
        elif key == 's-soltada':
            lib.frenar()
            print("s")
            
        elif key == 'd-presionada':
            lib.girar_derecha()
            print("d")

        elif key == 'd-soltada':
            lib.frenar()
            print("d")
             
        elif key == 'space':
            #lib.hablar()
            print("space")

        # Movimiento con los sticks
        if "Axis" in key:
            valores_axis = key.split()
            print(valores_axis)
            lib.movimiento_joystick(float(valores_axis[1]), float(valores_axis[2]))

        elif key == "up-soltado":
            #lib.avanzar()
            print("Up")

        elif key == "Up-presionada":
            lib.subir_garra()
        elif key == "Down-presionada":
            lib.bajar_garra()
        elif key == "Up-soltada":
            lib.parar_garra()
        elif key == "Down-soltada":
            lib.parar_garra()

        #Garra
        # elif key == "up-presionado":
        #     lib.subir_garra()
        #     print("Up")
        #
        # elif key == "up-soltado":
        #     #lib.avanzar()
        #     print("Up")
        #
        # elif key == "Down":
        #     #lib.girar_izquierda()
        #     print("Down")
        # elif key == "Left":
        #     #lib.girar_derecha()
        #     print("Left")
        # elif key == "Right":
        #     #lib.retroceder()
        #     print("Right")

        #Salir (q and BOTON_CENTRAL_MANDO)
        elif key == 'q-presionado':
            print('q')
            break

    print("Cerrando client")
    client.close()
    print("Cerrando socket")
    s.close()
