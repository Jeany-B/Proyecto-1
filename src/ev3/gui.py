import socket
import client
from tkinter import *
from tkinter import ttk

def mandar_input(event, socket_p):

    socket_p.sendall(event.keysym.encode())
    
    return

socket = client.retornar_socket()

#Ventana Principal
ventana_principal = Tk()
ventana_principal.title("EV3.")
ventana_principal.config(bg="#FF5757")
ventana_principal.geometry("800x700")
ventana_principal.resizable(0, 0)

ventana_principal.bind("<Key>", lambda event: mandar_input(event, socket))

ventana_principal.mainloop()
