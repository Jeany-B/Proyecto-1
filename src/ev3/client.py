import socket

def retornar_socket(ip_usuario_p):
    #"192.168.20.123"
    #"localhost"
    HOST = ip_usuario_p
    PORT = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))


    return s

def cortar_conexion(socket_p):
    socket_p.close()