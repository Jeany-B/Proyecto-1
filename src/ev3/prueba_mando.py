import pygame

#Joysticks
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]


pygame.init()
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        #Se reconoce el movimiento con la funcion JOYHBUTTONDOWN (botones principales)
        if event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(0).get_button(0):
                print("X")

            elif pygame.joystick.Joystick(0).get_button(1):
                print("O")

            elif pygame.joystick.Joystick(0).get_button(2):
                print("CUADRADO")

            elif pygame.joystick.Joystick(0).get_button(3):
                print("Triangulo")

        #Se reconoce el movimiento con la funcion JOYHATMOTION (flechitas)
        if event.type == pygame.JOYHATMOTION:
            x, y = event.value
            #Reconocer qué flecha es.
            #Izquierda-Derecha
            if (x == 1):
                print("Derecha")
            elif (x == -1):
                print("Izquierda")
            #Arriba-Abajo
            elif (y == 1):
                print("Arriba")
            elif (y == -1):
                print("Abajo")
            else:
                #print("Centro")
                pass
