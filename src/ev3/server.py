import socket

s = socket.socket()
print("Socket creado")
port = 8080
s.bind(('', port))
print(f"El socket se creó con puerto: {port}")
s.listen(4)
print("El socket está escuchando...")
client, addr = s.accept()
print(f"Se conectó a {addr}")

def moveUp():
    return

while True:
    rawByte = client.recv(1)
    char = rawByte.decode()

    match char:
        case 'w': 
            moveUp()
        case 'q':
            print("Cerrando conexión...")
            break

        case _:
            print("Tecla no soportada")
