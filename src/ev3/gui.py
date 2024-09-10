import socket
import client
from tkinter import *
from tkinter import ttk
import multiprocessing

def mandar_input(socket_p, mensaje):
    
    socket_p.sendall(mensaje)
    
    return

def gui_process(queue):
    def check_queue():
        try:

            # Verifica si hay algún mensaje en la cola y se ejecuta la funcion para mandarlo al servidor
            message = queue.get_nowait()
            mandar_input(socket, message.encode())

        except multiprocessing.queues.Empty:
            pass

        ventana_principal.after(100, check_queue)

    #Se crea el socket para conectarlo con el servidor y se guarda.
    socket = client.retornar_socket()
    print("Socket creado")

    #Ventana Principal
    ventana_principal = Tk()
    ventana_principal.title("EV3.")
    ventana_principal.config(bg="#FF5757")
    ventana_principal.geometry("800x700")
    ventana_principal.resizable(0, 0)

    #Label
    label_movimiento_ev3 = Label(ventana_principal, text="Movimiento EV3.")
    label_movimiento_ev3.place(x=10, y= 10)

    #Se manda las teclas del teclado si es que son presionadas
    ventana_principal.bind("<Key>", lambda event: mandar_input(socket, event.keysym.encode()))

    # Verificar la cola cada 100 ms
    ventana_principal.after(100, check_queue)

    # Ejecutar la ventana
    ventana_principal.mainloop()

if __name__ == "__main__":

    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()

    # Crear el proceso de tkinter
    gui_process(queue)

