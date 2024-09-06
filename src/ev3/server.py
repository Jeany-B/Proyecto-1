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

        if key == 'w':
            lib.avanzar()
        elif key == 'a':
            lib.girar_izquierda()
        elif key == 's':
            lib.retroceder()
        elif key == 'd':
            lib.girar_derecha()
        elif key == 'space':
            lib.hablar()
        elif key == "ARRIBA":
            lib.avanzar()
        elif key == "IZQUIERDA":
            print(key)
        elif key == "DERECHA":
            print(key)
        elif key == "ABAJO":
            print(key)
        elif key == "EQUIS":
            print(key)
        elif key == "O":
            print(key)
        elif key == "CUADRADO":
            print(key)
        elif key == "TRIANGULO":
            print(key)
        elif key == 'q':
            print('q')
            break

    print("Cerrando client")
    client.close()
    print("Cerrando socket")
    s.close()
