import pygame
import noise
import random
import math

pygame.init()

ANCHO = 1280
ALTURA = 768
ESCALA_RUIDO = 0.01
COLOR_TERRENO = (128, 64, 0)
semilla = random.randint(0, 50)
def generar_terreno(ANCHO_MUNDO,ALTURA_MUNDO):

    terreno = pygame.Surface((ANCHO_MUNDO, ALTURA_MUNDO))

    for x in range(ANCHO_MUNDO):
        # Determina la altura del terreno en este punto, el primer decimal para aumentar la altura de las montañas , el segundo para aumentar o disminuir el terreno
        altura = int(noise.pnoise1(x * ESCALA_RUIDO, base=semilla) * 0.3 * ALTURA_MUNDO + 0.5 * ALTURA_MUNDO)
        # Rellena el terreno hasta esta altura
        pygame.draw.line(terreno, COLOR_TERRENO, (x, ALTURA_MUNDO), (x, altura), 1)

    return terreno

def main():
    ANCHO_MUNDO = math.ceil(ANCHO/1.5)
    ALTURA_MUNDO = math.ceil(ALTURA/1.5)
    screen = pygame.display.set_mode((ANCHO, ALTURA), pygame.RESIZABLE,pygame.OPENGL)
    pygame.display.set_caption("Juego xd")
    textura_terreno = generar_terreno(ANCHO_MUNDO, ALTURA_MUNDO)

    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.VIDEORESIZE:  # Captura eventos de cambio de tamaño de ventana
                new_width, new_height = event.size
                screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)  # Cambia el tamaño de la ventana

        terreno_escalado = pygame.transform.scale(textura_terreno, (screen.get_width(), screen.get_height()))
        
        screen.blit(terreno_escalado, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()