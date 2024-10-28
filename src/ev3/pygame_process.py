import pygame
import multiprocessing
import time

def pygame_process(queue):
    
    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
    #Se verifica si ya hay un mando conectado
    if pygame.joystick.get_count() == 0:
        queue.put("Ningun mando conectado")
        return None
    
    joystick = pygame.joystick.Joystick(0)

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            # Módulo para saber si se desconectó un joystick o se conectó.
            if event.type == pygame.JOYDEVICEREMOVED:
                joystick.quit()
                queue.put("Disconnected")
            elif event.type == pygame.JOYDEVICEADDED:
                joystick.init()
                queue.put("Connected")

            #Se reconoce el movimiento con la funcion JOYHBUTTONDOWN (botones principales)
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(0):
                    print("Down")
                    queue.put("Down")

                elif pygame.joystick.Joystick(0).get_button(1):
                    print("Right")
                    queue.put("Right")

                elif pygame.joystick.Joystick(0).get_button(2):
                    print("Left")
                    queue.put("Left")

                elif pygame.joystick.Joystick(0).get_button(3):
                    print("Up")
                    queue.put("Up")

            #Se reconoce el movimiento con la funcion JOYHATMOTION (flechitas)
            if event.type == pygame.JOYHATMOTION:
                x, y = event.value
                #Reconocer qué flecha es.
                #Izquierda-Derecha
                if (x == 1):
                    print("d")
                    queue.put("d")
                elif (x == -1):
                    print("a")
                    queue.put("a")
                #Arriba-Abajo
                elif (y == 1):
                    print("w")
                    queue.put("w")
                elif (y == -1):
                    print("s")
                    queue.put("s")
                else:
                    #print("Centro")
                    pass
                    
        # Simular un retardo para la demostración
        #time.sleep(0.01)
    
    pygame.quit()

if __name__ == "__main__":
    
    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()
    # Crear el proceso de Pygame
    pygame_process(queue)