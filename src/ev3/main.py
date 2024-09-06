import multiprocessing
from gui import gui_process
from pygame_process import pygame_process

if __name__ == "__main__":
    # Crear la cola de comunicación
    queue = multiprocessing.Queue()

    # Crear los procesos
    tkinter_p = multiprocessing.Process(target=gui_process, args=(queue,))
    pygame_p = multiprocessing.Process(target=pygame_process, args=(queue,))

    # Iniciar los procesos
    tkinter_p.start()
    pygame_p.start()

    # Esperar a que ambos procesos terminen
    tkinter_p.join()
    pygame_p.join()
