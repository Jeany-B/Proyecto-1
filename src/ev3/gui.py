from tkinter import *
from tkinter import ttk

def mandar_input(event):
    print(":" + event.keysym)
    
    
    
    
    return


#Ventana Principal
ventana_principal = Tk()
ventana_principal.title("EV3.")
ventana_principal.config(bg="#FF5757")
ventana_principal.geometry("800x700")
ventana_principal.resizable(0,0)

ventana_principal.bind("<Key>", mandar_input)

ventana_principal.mainloop()