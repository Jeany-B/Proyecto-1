import socket
import client
from tkinter import *
from tkinter import ttk
import multiprocessing

def gui_process(queue):
    def check_queue():
        try:
            # Verifica si hay algún mensaje en la cola
            message = queue.get_nowait()
            label.config(text=f"Mensaje recibido: {message}")
        except multiprocessing.queues.Empty:
            pass
        ventana_principal.after(100, check_queue)

    #Ventana Principal
    ventana_principal = Tk()
    ventana_principal.title("EV3.")
    ventana_principal.config(bg="#FF5757")
    ventana_principal.geometry("800x700")
    ventana_principal.resizable(0, 0)

    #
    label = Label(ventana_principal, text="Esperando mensaje...")
    label.pack(padx=20, pady=20)

    #
    ventana_principal.bind("<Key>", lambda event: mandar_input(event, socket))

    # Verificar la cola cada 100 ms
    ventana_principal.after(100, check_queue)

    # Ejecutar la ventana
    ventana_principal.mainloop()

def mandar_input(event, socket_p):

    socket_p.sendall(event.keysym.encode())
    
    return

if __name__ == "__main__":

    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()

    # Crear el proceso de tkinter
    gui_process(queue)

    #Se crea el socket para conectarlo con el servidor y se guarda.
    socket = client.retornar_socket()
