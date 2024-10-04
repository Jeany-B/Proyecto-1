#!/usr/bin/env python3
# encoding=utf-8

import socket
#import library as lib

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

        #Teclado
        if key == 'w':
            #lib.avanzar()
            print("w")
        elif key == 'a':
            #lib.girar_izquierda()
            print("a")
        elif key == 's':
            #lib.retroceder()
            print("s")
        elif key == 'd':
            #lib.girar_derecha()
            print("d")
        elif key == 'space':
            #lib.hablar()
            print("space")
        #Mando
        elif key == "ARRIBA":
            #lib.avanzar()
            print("ARRIBA")
        elif key == "IZQUIERDA":
            #lib.girar_izquierda()
            print("IZQ")
        elif key == "DERECHA":
            #lib.girar_derecha()
            print("DEREC")
        elif key == "ABAJO":
            #lib.retroceder()
            print("ABAJ")
            
        elif key == "EQUIS":
            print(key)
        elif key == "O":
            print(key)
        elif key == "CUADRADO":
            print(key)
        elif key == "TRIANGULO":
            print(key)
        #Salir
        elif key == 'q':
            print('q')
            break

    print("Cerrando client")
    client.close()
    print("Cerrando socket")
    s.close()
