import pygame
import constantes
from Escribir import Escribir
from Boton import Boton
from configuraciones import Configuracion
import sys

class Configurar:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game
    def run(self):
        en_config = True
        font = pygame.font.Font(None, 42)
        change_delay = 100  # Milisegundos de retraso entre cambios
        last_change_time = 0
        ancho_botón, altura_botón = 0.10, 0.04
        margin_ratio = 0.05  # Margen de separación entre botones
        Volver = Boton(0.36 + ancho_botón / 2, 0.65 + 0.5 * altura_botón + margin_ratio, 0.18, 0.10, "Volver", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
        boton_dimenciones = [Boton(0.8 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, "->", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                            Boton(0.5 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, "<-", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)]
        while en_config:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Sal del menú

            keys = pygame.key.get_pressed()

            current_time = pygame.time.get_ticks()
            if current_time - last_change_time > change_delay:
                # Lógica para ajustar las opciones según las teclas presionadas
                if keys[pygame.K_UP]:
                    # Aumenta el número de jugadores (limitado a 6)
                    constantes.NUM_JUGADORES = min(constantes.NUM_JUGADORES + 1, 6)
                elif keys[pygame.K_DOWN]:
                    # Disminuye el número de jugadores (mínimo 2)
                    constantes.NUM_JUGADORES = max(constantes.NUM_JUGADORES - 1, 2)
                elif keys[pygame.K_RIGHT]:
                    # Aumenta el número de partidos
                    constantes.NUM_PARTIDAS = min(constantes.NUM_PARTIDAS + 1, 20)
                elif keys[pygame.K_LEFT]:
                    # Disminuye el número de partidos (mínimo 1)
                    constantes.NUM_PARTIDAS = max(constantes.NUM_PARTIDAS - 1, 1)
                elif keys[pygame.K_e]:
                    # Activa/desactiva los efectos del entorno
                    constantes.EFECTOS_ENTORNO = not constantes.EFECTOS_ENTORNO

                last_change_time = current_time
            if keys[pygame.K_RETURN]:
                Configuracion(constantes.NUM_JUGADORES,800,800,constantes.NUM_PARTIDAS)
            self.pantalla.fill((208, 237, 250))
            for boton in boton_dimenciones:
                boton.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
            Volver.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
            Escribir.render_text(self.pantalla, str(constantes.DIMENSIONES),(0.7 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio), 30, constantes.NEGRO,"Arial")
            Escribir.render_text(self.pantalla, "Ajustes del juego", (0.47 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
            # Muestra las opciones y valores en la pantalla
            Escribir.render_text(self.pantalla, f"Jugadores: {constantes.NUM_JUGADORES}", (0.016 + ancho_botón / 2, 0.28 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, "Use las flechas arriba y abajo para aumentar y disminuir los jugadores", (0.38 + ancho_botón / 2, 0.28 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"Número de Partidos: {constantes.NUM_PARTIDAS}", (0.05 + ancho_botón / 2, 0.32 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, "Use las flechas derecha e izquierda para aumentar y disminuir jugadores", (0.47 + ancho_botón / 2, 0.32 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"Efectos de Entorno: {'Activado' if constantes.EFECTOS_ENTORNO else 'Desactivado'}", (0.08 + ancho_botón / 2, 0.36 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"Dimensiones: {constantes.DIMENSIONES[0]},{constantes.DIMENSIONES[1]}", (0.06 + ancho_botón / 2, 0.4 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Volver.si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                            constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA = constantes.DIMENSIONES[0], \
                            constantes.DIMENSIONES[1]
                            self.gameStateManager.set_estado('menu')  
                            en_config = False     
                    if boton_dimenciones[1].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.DIMENSIONES[0] = int(constantes.config_defecto.ancho_pantalla)
                        constantes.DIMENSIONES[1] = int(constantes.config_defecto.alto_pantalla)
                    if boton_dimenciones[0].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.DIMENSIONES[0] = int(constantes.config_maximas.ancho_pantalla)
                        constantes.DIMENSIONES[1] = int(constantes.config_maximas.alto_pantalla)

            pygame.display.update()
            pygame.display.flip()
