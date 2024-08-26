import socket

HOST = "localhost"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall("Hola desde el cliente".encode())
    data = s.recv(1024)

print(f"Received {data}")
