import client
from tkinter import *
from tkinter import ttk
from tkinter import font
import multiprocessing
import time

def mandar_input(socket_p, mensaje):
    print(mensaje)
    
    if (socket_p == None):
        return
    else:
        socket_p.sendall(mensaje)  
        return

def gui_process(queue):

    #Funciones
    def check_queue():
        try:

            # Verifica si hay algún mensaje en la cola y se ejecuta la funcion para mandarlo al servidor
            message = queue.get_nowait()

            #Mando conectado/desconectado
            if (message == "Mando conectado"):
                
                ConectarMando("Mando conectado")
            elif (message == "Mando desconectado"):
                
                ConectarMando("Mando desconectado")
            else:
                #print(message)
                visualizar_botones_mando(message)
                mandar_input(socket, message.encode())

        except multiprocessing.queues.Empty:
            pass

        ventana_principal.after(100, check_queue)

    def crear_socket(ip_usuario_p):

        global socket
        try:
            
            print("Creando socket")
            #Se crea el socket para conectarlo con el servidor y se guarda.
            socket = client.retornar_socket(ip_usuario_p)
            print("Socket creado")

            #Se manda las teclas del teclado si es que son presionadas
            ventana_principal.bind("<KeyPress>", lambda event: mandar_input(socket, (event.keysym+"-presionada").encode()))
            ventana_principal.bind("<KeyRelease>", lambda event: mandar_input(socket, (event.keysym+"-soltada").encode()))

            #
            boton_conexion.config(text="Desconectar", fg="#009634", bg="#000000")

        except (TimeoutError, ConnectionRefusedError) as error:
            #
            boton_conexion.config(text="Volver a\nconectar.", fg="#800000", bg="#ff6363")

            #Se imprime el error y se desactiva la función para que reconozca las teclas del teclado.
            print("Error en la conexión con el EV3, vuelva a intentarlo.")
            ventana_principal.unbind("<Key>")


    def cambiar_gui_input(event):

        #Respectivamente, se activa y desactiva los botones/labels y relacionados a el input elegido del usuario
        if (combobox_input.get() == "Teclado"): 

            #Se desactivan los botones del mando
            canvas.itemconfigure(canva_fondo_mando, state='hidden')
            canvas.itemconfigure(canva_mando_xbox, state='hidden')
            boton_conectar_mando.place_forget()
            

            canvas.itemconfigure(canva_fondo_teclado, state='normal')
            #Label
            label_movimiento_ev3.place(x=80, y=170 + mover_conjunto)
            label_cortar_conexion.place(x=375, y=170 + mover_conjunto)
            label_garra.place(x=805, y=170 + mover_conjunto)
            label_sensor.place(x=300, y=400 + mover_conjunto)
            label_objeto_detectado.place(x=310, y=460 + mover_conjunto)
            label_conexion.place(x=580, y=400 + mover_conjunto)


            #Botones moverse            
            boton_w.place(x=150, y=250 + mover_conjunto)
            boton_s.place(x=150, y=300 + mover_conjunto)
            boton_a.place(x=100, y=300 + mover_conjunto)
            boton_d.place(x=200, y=300 + mover_conjunto)


            #Boton salir
            boton_q.place(x=490, y=270 + mover_conjunto)

            #Botones garra            
            boton_flecha_arriba.place(x=840, y=250 + mover_conjunto)
            boton_flecha_abajo.place(x=840, y=300 + mover_conjunto)
            boton_flecha_izquierda.place(x=790, y=300 + mover_conjunto)
            boton_flecha_derecha.place(x=890, y=300 + mover_conjunto)
            boton_conexion.place(x=618, y=460 + mover_conjunto)

            
        else:
            #Teclado olvidar
            canvas.itemconfigure(canva_fondo_teclado, state='hidden')
            #Label
            label_movimiento_ev3.place_forget()
            label_cortar_conexion.place_forget()
            label_garra.place_forget()

            #Botones moverse            
            boton_w.place_forget()
            boton_s.place_forget()
            boton_a.place_forget()
            boton_d.place_forget()


            #Botones
            boton_q.place_forget()

            #Botones garra            
            boton_flecha_arriba.place_forget()
            boton_flecha_abajo.place_forget()
            boton_flecha_izquierda.place_forget()
            boton_flecha_derecha.place_forget()
            boton_conexion.place_forget()

            #Mando
            canvas.itemconfig(canva_fondo_mando, state='normal')
            canvas.itemconfigure(canva_mando_xbox, state='normal')

            label_sensor.place(x=85, y=20)
            label_objeto_detectado.place(x=95, y=65)

            label_conexion.place(x=775, y=20)
            boton_conexion.place(x=812, y=70)

            boton_conectar_mando.place(x=419, y=570)
            
        ventana_principal.focus()
            

    def ventana_ingresar_ip():
        global socket

        if (socket == None):
            #Ventana
            ventana_ingresar_ip = Toplevel(ventana_principal)
            ventana_ingresar_ip.title("IP del EV3")
            ventana_ingresar_ip.geometry("300x300")
            ventana_ingresar_ip.config(bg="#471717")
            ventana_ingresar_ip.resizable(0, 0)

            #Variables
            fuente_ventana_secundaria = font.Font(family="Arial", size=15, weight="bold")

            #Widgets
            label_ingresar_ip = Label(ventana_ingresar_ip, text="Ingrese la IP del EV3", font=fuente_ventana_secundaria, bg=fondo_color_label, fg=letras_color_label)
            label_ingresar_ip.place(x=50, y=60)

            ip_usuario = Entry(ventana_ingresar_ip, width=25, font=("Arial", 12), justify="center")
            ip_usuario.place(x=35, y=120)

            boton_aceptar = Button(ventana_ingresar_ip, text="Aceptar", fg="#009634", bg="#D5FFE4", height=2, width=10, font=("Arial", 9, "bold"), command=lambda: crear_socket(ip_usuario.get()))
            boton_aceptar.place(x=50, y=180)

            boton_salir = Button(ventana_ingresar_ip, text="Salir", fg="#D70000", bg="#FFDDDD", height=2, width=10, font=("Arial", 9, "bold"), command=lambda: ventana_ingresar_ip.destroy())
            boton_salir.place(x=175, y=180)
        else:
            mandar_input(socket, "q".encode())
            socket = None
            ventana_principal.unbind("<Key>")
            boton_conexion.config(text="Conectar", fg="#009634", bg="#D5FFE4")

    def ConectarMando(message_p):
        
        if message_p == "Mando conectado":
            boton_conectar_mando.config(text="Mando conectado", fg="#009634", bg="#D5FFE4")
        elif message_p == "Mando desconectado":
            boton_conectar_mando.config(text="Mando desconectado", fg="#D70000", bg="#FFDDDD")
            
        



    def visualizar_botones_mando(boton_p):
        
        if (combobox_input.get() == "Teclado"): 
            return

        # Botones principales (Circulo, equis, etc)
        if (boton_p == "Up-presionada"):
            canvas.itemconfigure(canva_boton_arriba, state='normal')
            

        elif (boton_p == "Up-soltada"):
            canvas.itemconfigure(canva_boton_arriba, state='hidden')
            

        elif (boton_p == "Down-presionada"):
            canvas.itemconfigure(canva_boton_abajo, state='normal')
            
        elif (boton_p == "Down-soltada"):
            canvas.itemconfigure(canva_boton_abajo, state='hidden')
            
        elif (boton_p == "Right-presionada"):
            canvas.itemconfigure(canva_boton_derecha, state='normal')
            
        elif (boton_p == "Right-soltada"):
            canvas.itemconfigure(canva_boton_derecha, state='hidden')

        elif (boton_p == "Left-presionada"):
            canvas.itemconfigure(canva_boton_izquierda, state='normal')
        elif (boton_p == "Left-soltada"):
            canvas.itemconfigure(canva_boton_izquierda, state='hidden')

        # Botones de movimiento (flechitas)
        if (boton_p == "w-presionada"):
            canvas.itemconfigure(canva_flecha_arriba, state='normal')
            
        elif (boton_p == "w-soltada"):
            canvas.itemconfigure(canva_flecha_arriba, state='hidden')

        elif (boton_p == "s-presionada"):
            canvas.itemconfigure(canva_flecha_abajo, state='normal')
        elif (boton_p == "s-soltada"):
            canvas.itemconfigure(canva_flecha_abajo, state='hidden')

        elif (boton_p == "a-presionada"):
            canvas.itemconfigure(canva_flecha_izquierda, state='normal')
        elif (boton_p == "a-soltada"):
            canvas.itemconfigure(canva_flecha_izquierda, state='hidden')

        elif (boton_p == "d-presionada"):
            canvas.itemconfigure(canva_flecha_derecha, state='normal')
        elif (boton_p == "d-soltada"):
            canvas.itemconfigure(canva_flecha_derecha, state='hidden')



    #Variables
    global socket
    socket = None

    opciones_input = ["Teclado", "Mando"]
    opciones_sensor = ["Objeto\ndetectado", "Ningún objeto\ndetectado"]
    letras_color_botones = "white"
    fondo_color_botones = "#932022"

    fondo_color_label = "#471717"
    letras_color_label = "white"

    mover_conjunto = 50

    #Ventana Principal
    ventana_principal = Tk()
    ventana_principal.title("Ada")
    ventana_principal.geometry("1000x700")
    ventana_principal.config(bg="#471717")
    ventana_principal.resizable(0, 0)

    # Imagenes
    icono = PhotoImage(file="./data/images/CARA.png")
    logo = PhotoImage(file="./data/images/prueba1.png")
    

    fondo_teclado = PhotoImage(file="./data/images/Teclado.png")
    fondo_mando = PhotoImage(file="./data/images/Fondo_Mando.png")
    
    mando_xbox = PhotoImage(file="./data/images/Mando.png")

    flecha_arriba_presionada = PhotoImage(file="./data/images/F-Arriba.png")
    flecha_abajo_presionada = PhotoImage(file="./data/images/F-Abajo.png")
    flecha_derecha_presionada = PhotoImage(file="./data/images/F-Derecho.png")
    flecha_izquierda_presionada = PhotoImage(file="./data/images/F-Izquierdo.png")

    # Se le llama (arriba, abajo, etc), ya que la mayoria de mandos son distintos.
    boton_arriba_presionada = PhotoImage(file="./data/images/F-Ye.png")
    boton_abajo_presionada = PhotoImage(file="./data/images/F-A.png")
    boton_derecha_presionada = PhotoImage(file="./data/images/F-B.png")
    boton_izquierda_presionada = PhotoImage(file="./data/images/F-Equis.png")

    # Establecerlo como ícono de la ventana.
    ventana_principal.iconphoto(True, icono)



    #Canva y fondos
    canvas = Canvas(ventana_principal, width=1000, height=700)
    canvas.pack()

    canva_fondo_teclado = canvas.create_image(500, 355, image=fondo_teclado)
    canva_fondo_mando = canvas.create_image(500, 355, image=fondo_mando)    
    canvas.itemconfigure(canva_fondo_mando, state='hidden')

    canvas.create_rectangle(0, 0, 1000, 700, fill=fondo_color_label, stipple="gray75", outline="")

    canva_mando_xbox = canvas.create_image(500, 355, image=mando_xbox)
    canvas.itemconfigure(canva_mando_xbox, state='hidden')

    #Botones presionados (coloreados)
    canva_flecha_arriba = canvas.create_image(425, 330, image=flecha_arriba_presionada)
    canva_flecha_abajo = canvas.create_image(427, 386, image=flecha_abajo_presionada)
    canva_flecha_derecha = canvas.create_image(455, 356, image=flecha_derecha_presionada)
    canva_flecha_izquierda = canvas.create_image(396, 357, image=flecha_izquierda_presionada)

    canva_boton_arriba = canvas.create_image(646, 230, image=boton_arriba_presionada)
    canva_boton_abajo = canvas.create_image(646, 305, image=boton_abajo_presionada)
    canva_boton_derecha = canvas.create_image(685, 266, image=boton_derecha_presionada)
    canva_boton_izquierda = canvas.create_image(609, 265, image=boton_izquierda_presionada)

    canvas.itemconfigure(canva_flecha_arriba, state='hidden')
    canvas.itemconfigure(canva_flecha_abajo, state='hidden')
    canvas.itemconfigure(canva_flecha_derecha, state='hidden')
    canvas.itemconfigure(canva_flecha_izquierda, state='hidden')

    canvas.itemconfigure(canva_boton_arriba, state='hidden')
    canvas.itemconfigure(canva_boton_abajo, state='hidden')
    canvas.itemconfigure(canva_boton_derecha, state='hidden')
    canvas.itemconfigure(canva_boton_izquierda, state='hidden')


    
    #
    fuente = font.Font(family="Arial", size=20, weight="bold")

    #Label´s
    label_imagen = Label(ventana_principal, image=logo, bg=fondo_color_label)
    label_imagen.place(x=300, y=10)

    label_movimiento_ev3 = Label(ventana_principal, text="MOVIMIENTO", font=fuente, bg=fondo_color_label, fg=letras_color_label)
    label_movimiento_ev3.place(x=80, y=170 + mover_conjunto)

    label_cortar_conexion = Label(ventana_principal, text="CORTAR CONEXIÓN", font=fuente, bg=fondo_color_label, fg=letras_color_label)
    label_cortar_conexion.place(x=375, y=170 + mover_conjunto)

    label_garra = Label(ventana_principal, text="GARRA", font=fuente, bg=fondo_color_label, fg=letras_color_label)
    label_garra.place(x=805, y=170 + mover_conjunto)

    label_sensor = Label(ventana_principal, text="SENSOR", font=fuente, bg=fondo_color_label, fg=letras_color_label)
    label_sensor.place(x=300, y=400 + mover_conjunto)

    label_objeto_detectado = Label(ventana_principal, text=opciones_sensor[1], font=("Arial", 12), bg=fondo_color_label, fg="red")
    label_objeto_detectado.place(x=310, y=460 + mover_conjunto)

    label_conexion = Label(ventana_principal, text="CONEXIÓN", font=fuente, bg=fondo_color_label, fg=letras_color_label)
    label_conexion.place(x=580, y=400 + mover_conjunto)



    #Botones moverse
    boton_w = Button(ventana_principal, text="W", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "w".encode()))
    boton_w.place(x=150, y=250 + mover_conjunto)

    boton_s = Button(ventana_principal, text="S", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "s".encode()))
    boton_s.place(x=150, y=300 + mover_conjunto)

    boton_a = Button(ventana_principal, text="A", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "a".encode()))
    boton_a.place(x=100, y=300 + mover_conjunto)

    boton_d = Button(ventana_principal, text="D", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "d".encode()))
    boton_d.place(x=200, y=300 + mover_conjunto)

    #Boton cortar conexión
    boton_q = Button(ventana_principal, text="Q", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "q".encode()))
    boton_q.place(x=490, y=270 + mover_conjunto)

    #Botones garra
    boton_flecha_arriba = Button(ventana_principal, text="↑", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "Up".encode()))
    boton_flecha_arriba.place(x=840, y=250 + mover_conjunto)

    boton_flecha_abajo = Button(ventana_principal, text="↓", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "Down".encode()))
    boton_flecha_abajo.place(x=840, y=300 + mover_conjunto)

    boton_flecha_izquierda = Button(ventana_principal, text="←", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "Left".encode()))
    boton_flecha_izquierda.place(x=790, y=300 + mover_conjunto)

    boton_flecha_derecha = Button(ventana_principal, text="→", fg=letras_color_botones, bg=fondo_color_botones, height=2, width=4, font=("Arial", 10, "bold"), command=lambda: mandar_input(socket, "Right".encode()))
    boton_flecha_derecha.place(x=890, y=300 + mover_conjunto)

    boton_conexion = Button(ventana_principal, text="Conectar", fg="#009634", bg="#D5FFE4", height=2, width=10, font=("Arial", 9, "bold"), command=lambda: ventana_ingresar_ip())
    boton_conexion.place(x=618, y=460 + mover_conjunto)

    salir = Button(ventana_principal, text="Salir", fg="#D70000", bg="#FFDDDD", height=2, width=10, font=("Arial", 9, "bold"), command=lambda: ventana_principal.destroy())
    salir.place(x=900, y=640)


    #Mando
    boton_conectar_mando = Button(ventana_principal, text="Buscando mando...", fg="#6c6e01", bg="#fdff6e", font=("Arial", 11, "bold"), height=2, width=16)
    

    #ComboBox
    combobox_input = ttk.Combobox(ventana_principal, values=opciones_input, font=("Arial", 12, "bold"), state="readonly")
    combobox_input.set("Teclado")
    combobox_input.bind("<<ComboboxSelected>>", cambiar_gui_input)
    combobox_input.place(x=20, y=660)


    



    # Verificar la cola cada 100 ms
    ventana_principal.after(100, check_queue)

    ventana_principal.bind("<KeyPress>", lambda event: mandar_input(socket, (event.keysym+"-presionada").encode()))
    ventana_principal.bind("<KeyRelease>", lambda event: mandar_input(socket, (event.keysym+"-soltada").encode()))

    # Ejecutar la ventana
    ventana_principal.mainloop()

if __name__ == "__main__":

    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()

    # Crear el proceso de tkinter
    gui_process(queue)

