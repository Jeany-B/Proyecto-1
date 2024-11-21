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
                
                # If si se conectó un mando
                if event.type == pygame.JOYDEVICEADDED:
                    queue.put("Mando conectado")
                    pygame.joystick.init()
                    #print("Mando conectado")
                    running = False
                    break
                # Mensaje que todavía no hay mando conectado
                #print("mando desconectado")

    joystick = pygame.joystick.Joystick(0)
    posicion_anterior = (0, 0)


    running = True
    while running:
        event = pygame.event.wait()
        #print(event)

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYDEVICEREMOVED:
            #print("Mando desconectado")
            queue.put("Mando desconectado")
            joystick.quit()

        if event.type == pygame.JOYDEVICEADDED:
            #print("Mando conectado")
            queue.put("Mando conectado")
            joystick.init()
        
        #Se reconoce el movimiento con la funcion JOYHBUTTONDOWN (botones principales)
        if event.type == pygame.JOYBUTTONDOWN:
<<<<<<< HEAD
            
=======
>>>>>>> 176b9ded75acdd6803a88b228c9ba140ddb665b5
            if pygame.joystick.Joystick(0).get_button(0):
                print("x")
                queue.put("Si-Down")

            elif pygame.joystick.Joystick(0).get_button(1):
                print("o")
                queue.put("Right")

            elif pygame.joystick.Joystick(0).get_button(2):
                print("cua")
                queue.put("Left")

            elif pygame.joystick.Joystick(0).get_button(3):
                print("tri")
                queue.put("Up")
        
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print("No-Down")
            if event.button == 1:
                print("Se dejó de presionar o")
            if event.button == 2:
                print("Se dejó de presionar cua")
            if event.button == 3:
                print("Se dejó de presionar tri")

        #Se reconoce el movimiento con la funcion JOYHATMOTION (flechitas)
        if event.type == pygame.JOYHATMOTION:
<<<<<<< HEAD
            posicion_actual = joystick.get_hat(0)

            # Detectar cuando se presiona una dirección en el D-pad
            if posicion_actual != (0, 0) and posicion_anterior == (0, 0):
                print(f"Se presionó el D-pad en la dirección: {posicion_actual}")

            # Detectar cuando se suelta una dirección en el D-pad
            elif posicion_actual == (0, 0) and posicion_anterior != (0, 0):
                print(f"Se soltó el D-pad de la dirección: {posicion_anterior}")

            # Actualizar la posición anterior del D-pad
            posicion_anterior = posicion_actual


=======
>>>>>>> 176b9ded75acdd6803a88b228c9ba140ddb665b5
            x, y = event.value
            #Reconocer qué flecha es.
            #Izquierda-Derecha
            if (x == 1):
                queue.put("Si-d")
                print("d")
            elif (x == -1):
                queue.put("a")
                print("a")
            #Arriba-Abajo
            elif (y == 1):
                queue.put("w")
                print("w")
            elif (y == -1):
                queue.put("s")
                print("s")
            else:
                #queue.put()
                pass

                
        # Movimiento a través de los sticks
        if event.type == pygame.JOYAXISMOTION:
            x = joystick.get_axis(0)
            y = joystick.get_axis(1)

            # queue.put(f"Axis {x} {y}")
            print(f"x: {x}, y: {y}")

        # Simular un retardo para la demostración
        #time.sleep(0.01)
    
    pygame.quit()

if __name__ == "__main__":
    
    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()
    # Crear el proceso de Pygame
    pygame_process(queue)
