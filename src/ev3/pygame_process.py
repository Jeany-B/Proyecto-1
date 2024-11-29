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
            
            if pygame.joystick.Joystick(0).get_button(0):
                print("Down-presionada")
                queue.put("Down-presionada")

            elif pygame.joystick.Joystick(0).get_button(1):
                print("Right-presionada")
                queue.put("Right-presionada")

            elif pygame.joystick.Joystick(0).get_button(2):
                print("Left-presionada")
                queue.put("Left-presionada")

            elif pygame.joystick.Joystick(0).get_button(3):
                print("Up-presionada")
                queue.put("Up-presionada")
        
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print("Down-soltada")
                queue.put("Down-soltada")

            if event.button == 1:
                print("Right-soltada")
                queue.put("Right-soltada")
                
            if event.button == 2:
                print("Left-soltada")
                queue.put("Left-soltada")

            if event.button == 3:
                print("Up-soltada")
                queue.put("Up-soltada")

        #Se reconoce el movimiento con la funcion JOYHATMOTION (flechitas)
        if event.type == pygame.JOYHATMOTION:
            posicion_actual = joystick.get_hat(0)

            # Detectar cuando se presiona una dirección en el D-pad
            if posicion_actual != (0, 0) and posicion_anterior == (0, 0):
                if (posicion_actual == (0,1)):
                    print("w-presionada")
                    queue.put("w-presionada")

                elif (posicion_actual == (0, -1)):
                    print("s-presionado")
                    queue.put("s-presionada")

                elif (posicion_actual == (1,0)):
                    print("d-presionada")
                    queue.put("d-presionada")

                elif (posicion_actual == (-1,0)):
                    print("a-presionada")
                    queue.put("a-presionada")

                #print(f"Se presionó el D-pad en la dirección: {posicion_actual}")

            # Detectar cuando se suelta una dirección en el D-pad
            elif posicion_actual == (0, 0) and posicion_anterior != (0, 0):
                if (posicion_anterior == (0,1)):
                    print("w-soltada")
                    queue.put("w-soltada")

                elif (posicion_anterior == (0, -1)):
                    print("s-soltada")
                    queue.put("s-soltada")

                elif (posicion_anterior == (1,0)):
                    print("d-soltada")
                    queue.put("d-soltada")

                elif (posicion_anterior == (-1,0)):
                    print("a-soltada")
                    queue.put("a-soltada")

                #(f"Se soltó el D-pad de la dirección: {posicion_anterior}")

            # Actualizar la posición anterior del D-pad
            posicion_anterior = posicion_actual


                
        # Movimiento a través de los sticks
        if event.type == pygame.JOYAXISMOTION:
            x = joystick.get_axis(0)
            y = joystick.get_axis(1)

            if (x >= 0.1 and y >= 0.1):
                print(f"Axis {x} {y}")
                #queue.put(f"Axis {x} {y}")


        # Simular un retardo para la demostración
        #time.sleep(0.01)
    
    pygame.quit()

if __name__ == "__main__":
    
    # Cola para la comunicación entre procesos
    queue = multiprocessing.Queue()
    # Crear el proceso de Pygame
    pygame_process(queue)
