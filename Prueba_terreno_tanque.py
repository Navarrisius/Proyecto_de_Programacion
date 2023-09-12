
import pygame
import noise
import random
import math
import clases


def generar_terreno(x, altura_maxima, width):
    return altura_maxima * math.e ** (-((x - width) ** 2) / (2 * (width / 2) ** 2)) * math.cos(0.01 * (x - width)) + 200
def main():
    ANCHO_VENTANA = 1280
    ALTO_VENTANA = 768
    NOMBRE_VENTANA = "Juego XD"
    ANCHO_MUNDO = math.ceil(ANCHO_VENTANA/1.5)
    ALTURA_MUNDO = math.ceil(ALTO_VENTANA/1.5)
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE,pygame.OPENGL)
    game = clases.Partida()
    altura_terreno = [0] * ANCHO_VENTANA
    for x in range(ANCHO_VENTANA):
        altura_terreno[x] += generar_terreno(x, 200, ALTO_VENTANA)
    running = game.en_partida
    reloj = pygame.time.Clock()
    tecla_a_pulsada = False
    tecla_d_pulsada = False
    limite_angulo_min = 0
    limite_angulo_max = 180

    # Se inicia Pygame y se cambia el título de la ventana
    pygame.init()
    pygame.display.set_caption(NOMBRE_VENTANA)

    #Seting tanque
    tanque_1 = clases.Tanque("red")
    tanque_2 = clases.Tanque("blue")
    gravedad = 1
    tanque_1.posicion_x = 30
    tanque_1.posicion_y = 30
    tanque_2.posicion_x = 200*4
    tanque_2.posicion_y = 30
    radio = 30
    angulo_n = 0

    #Texto
    def escribir_texto(pantalla, texto, color_fuente, color_fondo, x, y):
        fuente = pygame.font.SysFont("consolas", 18)
        texto = fuente.render(texto, True, color_fuente, color_fondo)
        pantalla.blit(texto, (x, y))

    while running:
        # Captura todos los eventos dentro del juego
        for event in pygame.event.get():
            # Captura el cierre de la ventana
            if event.type == pygame.QUIT:
                running = False
            # Captura eventos de cambio de tamaño de ventana
            if event.type == pygame.VIDEORESIZE: 
                NUEVO_ANCHO, NUEVA_ALTURA = event.size
                # Cambia el tamaño de la ventana
                pantalla = pygame.display.set_mode((NUEVO_ANCHO, NUEVA_ALTURA), pygame.RESIZABLE,pygame.OPENGL)
            teclas = pygame.key.get_pressed()
            # Verifica si la tecla 'A' se mantiene presionada
            if teclas[pygame.K_a]:
                tecla_a_pulsada = True
                angulo_n += 0.5
                if angulo_n > limite_angulo_max:
                    angulo_n = limite_angulo_max
            else:
                tecla_a_pulsada = False
            # Verifica si la tecla 'D' se mantiene presionada
            if teclas[pygame.K_d]:
                tecla_d_pulsada = True
                angulo_n -= 0.5
                if angulo_n < limite_angulo_min:
                    angulo_n = limite_angulo_min
            else:
                tecla_d_pulsada = False
            # Actualiza el ángulo
            if tecla_a_pulsada:
                angulo = math.radians(angulo_n)
            if tecla_d_pulsada:
                angulo = math.radians(angulo_n)
        #VACIA PANTALLA
        pantalla.fill((0, 0, 0))

        # Mantener el tanque en el terreno
        tanque_1.posicion_y = ALTO_VENTANA - altura_terreno[tanque_1.posicion_x]
        tanque_2.posicion_y = ALTO_VENTANA - altura_terreno[tanque_2.posicion_x]

        angulo = (math.radians(angulo_n))
        #terreno
        for x in range(ANCHO_VENTANA):
            pygame.draw.rect(pantalla, (0, 255, 0), (x, ALTO_VENTANA - altura_terreno[x], 1, altura_terreno[x]))

        escribir_texto(pantalla=pantalla, texto="Ángulo: " + str(angulo_n) + "°", color_fuente=(255, 255, 255), color_fondo=(0, 0, 255), x=tanque_1.posicion_x + 100, y=tanque_1.posicion_y)
        def draw_tank(screen, tanque):
            tank_points = [(tanque.posicion_x - 50 // 2, tanque.posicion_y),(tanque.posicion_x - 50 // 2, tanque.posicion_y - 10),
                           (tanque.posicion_x - 50 // 2 + 5, tanque.posicion_y - 13),(tanque.posicion_x + 50 // 2 - 5, tanque.posicion_y - 13),
                           (tanque.posicion_x + 50 // 2, tanque.posicion_y - 10),(tanque.posicion_x + 50 // 2, tanque.posicion_y)]
            pygame.draw.polygon(screen, tanque.color, tank_points)
            # Dibuja la torreta del tanque
            turret_length = 30
            turret_start = (tanque.posicion_x, tanque.posicion_y - 10)
            turret_end = (tanque.posicion_x + turret_length * math.cos(angulo),tanque.posicion_y - 10 - turret_length * math.sin(angulo))
            pygame.draw.line(screen, (150,150,150), turret_start, turret_end, 4)
        #Agregar tanque
        draw_tank(pantalla, tanque_1)
        draw_tank(pantalla, tanque_2)
        #pygame.draw.rect(pantalla,(0, 255, 0), (tanque_1.posicion_x, tanque_1.posicion_y, 50, 30))
        #pygame.draw.line(pantalla, (150, 150, 150),(tanque_1.posicion_x, tanque_1.posicion_y), (x1, y1), 10)

        pygame.display.flip()
        # Limita los FPS a 60
        reloj.tick(60)

    pygame.quit()

main()