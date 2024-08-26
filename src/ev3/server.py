import socket

HOST = "localhost"
PORT = 8080

# Creación y setup de socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket creado")
    s.bind((HOST, PORT))
    print(f"El socket se creó con puerto: {PORT}")
    s.listen(4)
    print("El socket está escuchando...")

    # Se espera la conexión con el cliente
    client, addr = s.accept()
    print(f"Se conectó a {addr}")

    # Main loop
    while True:
        # Se recibe un byte y se decodifica
        data = client.recv(128)
        char = data.decode()

        match char:
            case 'w': 
                print('w')
            case 'a':
                print('a')
            case 's':
                print('s')
            case 'd':
                print('d')
            case 'q':
                print("Cerrando conexión...")
                break

            case _:
                print("Tecla no soportada")

    client.close()
