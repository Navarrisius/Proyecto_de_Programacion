import pygame
import constantes
import funciones
from Bala import Bala
from Fondo import Fondo
from Terreno import Terreno
from UI import UI

class EnPartida:
    def __init__(self, pantalla, gameStateManager,game):
        self.gameStateManager = gameStateManager
        self.pantalla = pantalla
        self.game = game
    def run(self):
        global reloj
        pygame.mixer.init()
        pygame.mixer.music.load('mp3/C418_Living_Mice.mp3')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        constantes.JUGADORES = []
        constantes.MUSICA = 'mp3/C418_Living_Mice.mp3'
        funciones.crear_jugadores()
        turno = None
        constantes.TERRENO = Terreno()
        fondo = Fondo()
        running = self.game.en_partida
        pygame.time.Clock()
        ui = UI()
        img_reiniciar = pygame.image.load("img/reiniciar.png")
        img_reiniciar = pygame.transform.scale(img_reiniciar, (64, 64))
        img_terminar_partida = pygame.image.load("img/terminar_partida.png")
        img_terminar_partida = pygame.transform.scale(img_terminar_partida, (70, 70))
        img_musica = pygame.image.load("img/musica.png")
        img_musica = pygame.transform.scale(img_musica, (70, 70))
        img_linea_diagonal_sin_musica = pygame.image.load("img/linea_diagonal.png")
        altura_terreno = constantes.TERRENO.generar_terreno_perlin(constantes.DIMENSIONES[0])
        constantes.TERRENO.generar_matriz(constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA, altura_terreno)
        funciones.iniciar_tanques(constantes.TERRENO)
        funciones.definir_turnos()

        while running:
            turno = constantes.ARRAY_TURNOS[constantes.TURNO_ACTUAL]
            reloj = pygame.time.Clock()
            teclas = pygame.key.get_pressed()
            if constantes.EN_RONDA_DE_COMPRA:
                if constantes.MUSICA != 'mp3/C418_Living_Mice.mp3':
                    funciones.cambiar_musica('mp3/C418_Living_Mice.mp3')
                    constantes.MUSICA = 'mp3/C418_Living_Mice.mp3'
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: 
                            clic_x, clic_y = pygame.mouse.get_pos()
                            # Verificar si el clic ocurrió dentro de la imagen, ir a menu
                            if constantes.ANCHO_VENTANA - 100 <= clic_x <= constantes.ANCHO_VENTANA - 30 and 40 <= clic_y <= 37 + 64:
                                pygame.mixer.music.load('mp3/aria_math.mp3')
                                pygame.mixer.music.set_volume(0.1)
                                pygame.mixer.music.play(-1)
                                funciones.limpiar_constantes()
                                self.gameStateManager.set_estado('menu')
                                running = False
                            # Verificar si el clic ocurrió dentro de la imagen, reiniciar juego
                            if constantes.ANCHO_VENTANA - 200 <= clic_x <= constantes.ANCHO_VENTANA - 136 and 40 <= clic_y <= 40 + 64:
                                funciones.limpiar_constantes()
                                self.run()
                    funciones.detectar_musica(event)
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.VIDEORESIZE:
                        NUEVO_ANCHO, NUEVA_ALTURA = event.size
                        self.pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE, pygame.OPENGL)
                        constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA = NUEVO_ANCHO, NUEVA_ALTURA
                    elif teclas[pygame.K_ESCAPE]:
                        running = funciones.pausar(self)
                        if running == False:
                            funciones.limpiar_constantes()
                    funciones.controles_compra(teclas, turno)
                    funciones.combrobar_compra_de_todos_los_jugadores()
            else:
                for event in pygame.event.get():
                    funciones.saltar_turno_tanque_sin_municion(turno)
                    if constantes.MUSICA != 'mp3/Death_by_Glamour.mp3':
                        funciones.cambiar_musica('mp3/Death_by_Glamour.mp3')
                        constantes.MUSICA = 'mp3/Death_by_Glamour.mp3'
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: 
                            clic_x, clic_y = pygame.mouse.get_pos()
                            # Verificar si el clic ocurrió dentro de la imagen, ir a menu
                            if constantes.ANCHO_VENTANA - 100 <= clic_x <= constantes.ANCHO_VENTANA - 30 and 40 <= clic_y <= 37 + 64:
                                pygame.mixer.music.load('mp3/aria_math.mp3')
                                pygame.mixer.music.set_volume(0.1)
                                pygame.mixer.music.play(-1)
                                funciones.limpiar_constantes()
                                self.gameStateManager.set_estado('menu')
                                running = False
                            # Verificar si el clic ocurrió dentro de la imagen, reiniciar juego
                            if constantes.ANCHO_VENTANA - 200 <= clic_x <= constantes.ANCHO_VENTANA - 136 and 40 <= clic_y <= 40 + 64:
                                funciones.limpiar_constantes()
                                self.run()
                    funciones.detectar_musica(event)
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.VIDEORESIZE:
                        NUEVO_ANCHO, NUEVA_ALTURA = event.size
                        self.pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE, pygame.OPENGL)
                        constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA = NUEVO_ANCHO, NUEVA_ALTURA
                    elif teclas[pygame.K_ESCAPE]:
                        running = funciones.pausar(self)
                        if running == False:
                            funciones.limpiar_constantes()
                    funciones.controles(event, teclas, turno, constantes.TANQUES, constantes.TERRENO, self.game)

            # VACIA PANTALLA
            fondo.cargar_fondo(self.pantalla, 1)

            # Mantener el tanque en el terreno y comprobar caida
            for jugador in constantes.JUGADORES:
                jugador.tanque.posicion_y = funciones.calcular_y(constantes.TERRENO.matriz, jugador.tanque)
                if jugador.tanque.posicion_y != jugador.tanque.caida_tanque:
                    jugador.tanque.calcular_damage_caida(jugador.tanque.caida_tanque)
                    ui.mensaje_caida(pantalla=self.pantalla, ancho=constantes.ANCHO_VENTANA, diff_y=abs(jugador.tanque.posicion_y - jugador.tanque.caida_tanque))
                    jugador.tanque.caida_tanque = jugador.tanque.posicion_y

            for jugador in constantes.JUGADORES :
                if jugador.tanque.salud <= 0 :
                    jugador.tanque.corregir_salud()
                    jugador.vivo = False

            # Terreno
            constantes.TERRENO.dibujar_terreno(self.pantalla)
            ui.barras_de_salud(self.pantalla)
            

            funciones.ui_pre_disparo(ui, self.pantalla, turno)

            ui.texto_jugador(self.pantalla, turno.tanque.color, turno.nombre)

            self.game.ganador = funciones.definir_ganador()


            # Texto con el jugador ganador
            if (self.game.ganador is not None) and constantes.NUM_PARTIDAS == constantes.RONDA_ACTUAL-1:
                pygame.mixer.music.stop()
                # Esperar 5 segundos antes de cerrar la ventana
                tiempo_inicial = pygame.time.get_ticks()
                tiempo_espera = 5000
                while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                    pygame.display.update()
                    termino = funciones.terminar_de_juego(self)
                    if termino == False:
                            funciones.limpiar_constantes()
                            running = False
                    elif termino == 1:
                        funciones.limpiar_constantes()
                        self.run()
                pygame.display.update()
                
            else:
                # Botón reinicio
                self.pantalla.blit(img_reiniciar, (constantes.ANCHO_VENTANA - 200, 40))

                # Botón término partida
                self.pantalla.blit(img_terminar_partida, (constantes.ANCHO_VENTANA - 100, 37))

                # Botón música
                if constantes.MUSICA_PARTIDA:
                    self.pantalla.blit(img_musica, (constantes.ANCHO_VENTANA - 300, 37))
                else:
                    self.pantalla.blit(img_musica, (constantes.ANCHO_VENTANA - 300, 37))
                    self.pantalla.blit(img_linea_diagonal_sin_musica, (constantes.ANCHO_VENTANA - 297, 40))

                for jugador in constantes.JUGADORES :
                    jugador.tanque.draw_tank(self.pantalla)

            if constantes.DISPARO is not None:
                disparo = constantes.DISPARO
                disparo.recorrido(self.pantalla, turno.tanque.color)
                ui.info_bala(self.pantalla, -1, int(disparo.altura_maxima), int(disparo.distancia_maxima))
                pygame.display.update()
                # Esperar 2 segundos
                tiempo_inicial = pygame.time.get_ticks()
                tiempo_espera = 2000
                while pygame.time.get_ticks() - tiempo_inicial < tiempo_espera:
                    pass
                constantes.DISPARO = None
            
            if constantes.EN_RONDA_DE_COMPRA:
                ui.ronda_compra(self.pantalla, constantes.ANCHO_VENTANA)
            
            funciones.combrobar_municion_tanques()
            funciones.comprobar_jugadores_vivos()

            pygame.display.flip()

            # Limita los FPS a 60
            reloj.tick(60)
            for jugador in constantes.JUGADORES:
                print(f"{jugador.nombre}: {jugador.kills} kills, {jugador.tanque.salud} HP")
            ganador = funciones.definir_ganador()
            ui.pantalla_ganador(ganador)
