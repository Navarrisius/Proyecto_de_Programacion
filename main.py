import pygame

def main():
    ANCHO_VENTANA = 1280
    ALTO_VENTANA = 720
    NOMBRE_VENTANA = "Juego XD"
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    running = True
    reloj = pygame.time.Clock()

    # Se inicia Pygame y se cambia el título de la ventana
    pygame.init()
    pygame.display.set_caption(NOMBRE_VENTANA)

    while running:

        # Captura todos los eventos dentro del juego
        for event in pygame.event.get():

            # Captura el cierre de la ventana
            if event.type == pygame.QUIT:
                running = False

        # Limita los FPS a 60
        reloj.tick(60) 

        pantalla.fill((255, 255, 255))

        pygame.display.flip()


main()