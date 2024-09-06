import pygame
import multiprocessing
import time

def pygame_process(queue):
    pygame.init()

    # Crear la ventana de Pygame
    #screen = pygame.display.set_mode((640, 480))
    #pygame.display.set_caption("Pygame Window")

    #Joysticks
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            #Se reconoce el movimiento con la funcion JOYHBUTTONDOWN (botones principales)
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(0):
                    queue.put("EQUIS")

                elif pygame.joystick.Joystick(0).get_button(1):
                    queue.put("O")

                elif pygame.joystick.Joystick(0).get_button(2):
                    queue.put("CUADRADO")

                elif pygame.joystick.Joystick(0).get_button(3):
                    queue.put("TRIANGULO")

            #Se reconoce el movimiento con la funcion JOYHATMOTION (flechitas)
            if event.type == pygame.JOYHATMOTION:
                x, y = event.value
                #Reconocer qué flecha es.
                #Izquierda-Derecha
                if (x == 1):
                    queue.put("DERECHA")
                elif (x == -1):
                    queue.put("IZQUIERDA")
                #Arriba-Abajo
                elif (y == 1):
                    queue.put("ARRIBA")
                elif (y == -1):
                    queue.put("ABAJO")
                else:
                    #print("Centro")
                    pass
                    
        #screen.fill((0, 0, 0))
        #pygame.display.flip()

        # Simular un retardo para la demostración
        time.sleep(0.01)

    pygame.quit()

if __name__ == "__main__":
    
    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()
    # Crear el proceso de Pygame
    pygame_process(queue)