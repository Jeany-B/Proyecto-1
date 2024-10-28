import pygame
import multiprocessing
import time

def pygame_process(queue):
    
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.JOYDEVICEADDED:
                    pygame.joystick.init()
                    print("Mando conectado")
                    running = False
                    break

    joystick = pygame.joystick.Joystick(0)

    running = True
    while running:
        event = pygame.event.wait()
        print(event)

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYDEVICEREMOVED:
            joystick.quit()
            print("Mando desconectado")

        if event.type == pygame.JOYDEVICEADDED:
            joystick.init()
            print("Mando conectado")
        
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
                

        # Simular un retardo para la demostración
        #time.sleep(0.01)
    
    pygame.quit()

if __name__ == "__main__":
    
    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()
    # Crear el proceso de Pygame
    pygame_process(queue)
