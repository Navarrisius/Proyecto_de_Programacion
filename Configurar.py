import pygame
import constantes
from Escribir import Escribir
from Boton import Boton
from Configuracion import Configuracion
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
        Volver = Boton(0.36 + ancho_botón / 2, 0.75 + 0.5 * altura_botón + margin_ratio, 0.18, 0.10, "Volver", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)
        boton_dimenciones = [Boton(0.69 + ancho_botón / 2, 0.33 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, ">", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                            Boton(0.45 + ancho_botón / 2, 0.33 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, "<", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.05 + ancho_botón / 2, 0.33 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, "<",constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.25 + ancho_botón / 2, 0.33 - 0.5 * altura_botón + margin_ratio, ancho_botón, altura_botón, ">",constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.05 + ancho_botón / 2, 0.48 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, "<", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.25 + ancho_botón / 2, 0.48 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, ">", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.05 + ancho_botón / 2, 0.63 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, "<", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.25 + ancho_botón / 2, 0.63 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, ">", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.45 + ancho_botón / 2, 0.48 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, "<", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.69 + ancho_botón / 2, 0.48 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, ">", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.45 + ancho_botón / 2, 0.63 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, "<", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50),
                             Boton(0.69 + ancho_botón / 2, 0.63 - 0.5 * altura_botón + margin_ratio, ancho_botón,altura_botón, ">", constantes.BLANCO, constantes.CELESTE, constantes.NEGRO, 50)]
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


            last_change_time = current_time
            if keys[pygame.K_RETURN]:
                Configuracion(constantes.NUM_JUGADORES,800,800,constantes.NUM_PARTIDAS)
            self.pantalla.fill((208, 237, 250))
            for boton in boton_dimenciones:
                boton.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
            Volver.dibujar(self.pantalla, constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
            Escribir.render_text(self.pantalla, "Ajustes del juego", (0.47 + ancho_botón / 2, 0.07 - 0.5 * altura_botón + margin_ratio), 60, constantes.NEGRO, "More Sugar")
            # Muestra las opciones y valores en la pantalla
            Escribir.render_text(self.pantalla, "Jugadores", (0.2 + ancho_botón / 2, 0.28 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"{constantes.NUM_JUGADORES}", (0.2 + ancho_botón / 2, 0.35 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"Número de Partidos", (0.2 + ancho_botón / 2, 0.43 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"{constantes.NUM_PARTIDAS}", (0.2 + ancho_botón / 2, 0.5 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, "CPU",(0.2 + ancho_botón / 2, 0.57 - 0.5 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, f"{constantes.NUM_CPU}",(0.2 + ancho_botón / 2, 0.64 - 0.57 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
            #Escribir.render_text(self.pantalla, f"Efectos de Entorno: {'Activado' if constantes.EFECTOS_ENTORNO else 'Desactivado'}", (0.08 + ancho_botón / 2, 0.36 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO, None)
            Escribir.render_text(self.pantalla,"Resolucion",(0.62 + ancho_botón / 2, 0.28 - 0.5 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, str(constantes.DIMENSIONES),(0.62 + ancho_botón / 2, 0.35 - 0.5 * altura_botón + margin_ratio), 20, constantes.NEGRO,"Arial")
            Escribir.render_text(self.pantalla, "Efectos de Entorno",(0.62 + ancho_botón / 2, 0.43 - 0.5 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
            Escribir.render_text(self.pantalla,f"{'Activado' if constantes.EFECTOS_ENTORNO else 'Desactivado'}",(0.62 + ancho_botón / 2, 0.50 - 0.5 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
            Escribir.render_text(self.pantalla, "Gravedad",(0.62 + ancho_botón / 2, 0.57 - 0.5 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
            Escribir.render_text(self.pantalla,f"{round(constantes.GRAVEDAD, 1)} m/s^2",(0.62 + ancho_botón / 2, 0.64 - 0.57 * altura_botón + margin_ratio), 20,constantes.NEGRO, None)
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
                    if boton_dimenciones[2].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.NUM_JUGADORES = max(constantes.NUM_JUGADORES - 1, 0)
                    if boton_dimenciones[3].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.NUM_JUGADORES = min(constantes.NUM_JUGADORES + 1, 6)
                    if boton_dimenciones[4].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.NUM_PARTIDAS = max(constantes.NUM_PARTIDAS - 1, 1)
                    if boton_dimenciones[5].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.NUM_PARTIDAS = min(constantes.NUM_PARTIDAS + 1, 20)
                    if boton_dimenciones[6].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.NUM_CPU = max(constantes.NUM_CPU - 1, 0)
                    if boton_dimenciones[7].si_clic(constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA):
                        constantes.NUM_CPU = min(constantes.NUM_CPU + 1, 6)
                    if boton_dimenciones[8].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.EFECTOS_ENTORNO = not constantes.EFECTOS_ENTORNO
                    if boton_dimenciones[9].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.EFECTOS_ENTORNO = not constantes.EFECTOS_ENTORNO
                    if boton_dimenciones[10].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.GRAVEDAD = max(constantes.GRAVEDAD - 1,1)
                    if boton_dimenciones[11].si_clic(constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA):
                        constantes.GRAVEDAD = min(constantes.GRAVEDAD + 1,50)




            pygame.display.update()
            pygame.display.flip()
