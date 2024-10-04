import pygame
import multiprocessing
import time

def pygame_process(queue):
    
    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    def conectar_mando():
        #pygame.joystick.quit()  # Reinicia el módulo de joystick para detectar nuevos dispositivos
        pygame.joystick.init()
        
        #Comprobar si hay algun mando conectado
        while not pygame.joystick.get_count() > 0:
            #queue.put("Disconnected")
            print("descon")
            time.sleep(3)
            #pygame.joystick.quit()
            pygame.joystick.init()

        print("conect")
        #queue.put("Connected")
    
    conectar_mando()

    # Define el tamaño de la ventana
    ancho = 640
    alto = 480

    # Crea la ventana con las dimensiones especificadas
    pantalla = pygame.display.set_mode((ancho, alto))

    # Título de la ventana
    pygame.display.set_caption("Ventana Simple")

    # Color de fondo (RGB)
    color_fondo = (0, 128, 255)  # Azul claro

    
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            if not pygame.joystick.get_count() > 0:
                print("Mando desconecado")
                #conectar_mando()

            #Se reconoce el movimiento con la funcion JOYHBUTTONDOWN (botones principales)
            if event.type == pygame.JOYBUTTONDOWN:
                print("1if")
                if pygame.joystick.Joystick(0).get_button(0):
                    print("x")
                    #queue.put("EQUIS")

                elif pygame.joystick.Joystick(0).get_button(1):
                    print("o")
                    #queue.put("O")

                elif pygame.joystick.Joystick(0).get_button(2):
                    print("cua")
                    #queue.put("CUADRADO")

                elif pygame.joystick.Joystick(0).get_button(3):
                    print("tri")
                    #queue.put("TRIANGULO")

            #Se reconoce el movimiento con la funcion JOYHATMOTION (flechitas)
            if event.type == pygame.JOYHATMOTION:
                print("2if")
                x, y = event.value
                #Reconocer qué flecha es.
                #Izquierda-Derecha
                if (x == 1):
                    #queue.put("DERECHA")
                    print("de")
                elif (x == -1):
                    #queue.put("IZQUIERDA")
                    print("izq")
                #Arriba-Abajo
                elif (y == 1):
                    #queue.put("ARRIBA")
                    print("arrib")
                elif (y == -1):
                    #queue.put("ABAJO")
                    print("abaj")
                else:
                    #print("Centro")
                    pass
                    

        # Rellena la pantalla con el color de fondo
        pantalla.fill(color_fondo)
        
        # Actualiza la pantalla
        pygame.display.flip()

        # Simular un retardo para la demostración
        #time.sleep(0.01)
    
    pygame.quit()

if __name__ == "__main__":
    
    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()
    # Crear el proceso de Pygame
    pygame_process(queue)