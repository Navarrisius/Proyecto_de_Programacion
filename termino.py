import pygame
import constantes
from Boton import Boton
import sys
from Escribir import Escribir

class Termino:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game
    def run(self):
        self.pantalla.fill((225, 225, 208))
        ancho_botón, altura_botón = 0.25, 0.08  # Margen de separación entre botones
        margin_ratio = 0.05
        Escribir.render_text(self.pantalla, "Juego terminado", (0.35 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
        botones = [
            Boton(0.5 - ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón,
                altura_botón, "Salir",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
            Boton(0.5 - ancho_botón / 2, 0.5 + 1.5 * altura_botón, ancho_botón, altura_botón, "Reiniciar",
                constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)]
        termino = True
        pygame.display.flip()
        pygame.display.update()
        while termino:
            reloj = pygame.time.Clock()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botones[0].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                            self.gameStateManager.set_estado('menu')
                            termino = False 
                            return termino
                    if botones[1].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                            self.gameStateManager.set_estado('partida')
                            termino = False
                            return 1

            for boton in botones:
                boton.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)

            pygame.display.flip()
             
        reloj.tick(5)