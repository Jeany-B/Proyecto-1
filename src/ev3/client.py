import socket
from tkinter import *
from tkinter import ttk

HOST = "localhost"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def mandar_input(event):
    s.sendall(event.keysym.encode())
    return


#Ventana Principal
ventana_principal = Tk()
ventana_principal.title("EV3.")
ventana_principal.config(bg="#FF5757")
ventana_principal.geometry("800x700")
ventana_principal.resizable(0, 0)

ventana_principal.bind("<Key>", mandar_input)

ventana_principal.mainloop()
