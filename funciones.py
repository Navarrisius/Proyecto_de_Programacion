import pygame
import math
from Bala import Bala
from Disparo import Disparo
from Jugador import Jugador
from Partida import Partida
from Compra import Compra
from Tanque import Tanque
from Pausa import Pausa
from Termino import Termino
import constantes
import random

def posicion(x,y,ancho_botón,altura_botón,margin_ratio):
    pos_x_rel = x + ancho_botón / 2
    pos_y_rel = y - 0.5 * altura_botón + margin_ratio
        # Calcula las coordenadas en función de la resolución actual
    pos_x = constantes.ANCHO_VENTANA * pos_x_rel
    pos_y = constantes.ALTO_VENTANA * pos_y_rel
    return pos_x, pos_y

def actualizar_info_pantalla():
    info = pygame.display.Info()
    constantes.ANCHO_VENTANA = info.current_w
    constantes.ALTO_VENTANA = info.current_h

def crear_jugadores():
    colores_rgb = {
        "verde_musgo": (47, 69, 56),
        "rojo": (255, 0, 0),
        "azul": (0, 0, 255),
        "rosado": (252, 3, 186),
        "negro": (0, 0, 0),
        "morado" : (99, 11, 87)
    }
    pos_inicial = 0
    pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.NUM_JUGADORES
    colores_disponibles = list(colores_rgb.values())
    for i in range(constantes.NUM_JUGADORES) :
        color = random.choice(colores_disponibles)
        colores_disponibles.remove(color)
        jugador = Jugador(None, Tanque(color))
        jugador.tanque.posicion_x = random.randint(pos_inicial, pos_final)
        jugador.tanque.posicion_y = 30
        jugador.tanque.angulo_canon = 0
        constantes.JUGADORES.append(jugador)
        pos_inicial = pos_final
        pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.NUM_JUGADORES
    elegir_nombres()


def calcular_y(matriz, tanque):
    for y in range(len(matriz)):
        if (matriz[y][tanque.posicion_x] == "x"):
            return y - 1
        

def definir_turnos():
    constantes.ARRAY_TURNOS = constantes.JUGADORES.copy()
    random.shuffle(constantes.ARRAY_TURNOS)
    for jugador in constantes.ARRAY_TURNOS:
        constantes.TANQUES.append(jugador.tanque)
        jugador.puede_jugar = False


def cambiar_turno():
    constantes.TURNO_ACTUAL += 1
    if constantes.TURNO_ACTUAL >= constantes.NUM_JUGADORES:
        constantes.TURNO_ACTUAL = 0


def elegir_nombres():
    nombres = ["Pessi", "Penaldo", "Bendepan", "Empujaland", "Abuelowski", "Fictisius Jr"]
    for jugador in constantes.JUGADORES:
        nombre = random.choice(nombres)
        nombres.remove(nombre)
        jugador.nombre = nombre
    

def pausar(self):
    return Pausa.run(self)

def terminar_de_juego(self,conclusion):
    return Termino.run(self,conclusion)

def detectar_musica(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
            clic_x, clic_y = pygame.mouse.get_pos()
            # Verificar si el clic ocurrió dentro de la imagen
            if constantes.ANCHO_VENTANA - 300 <= clic_x <= constantes.ANCHO_VENTANA - 230 and 40 <= clic_y <= 37 + 64:
                if constantes.MUSICA_PARTIDA:
                    pygame.mixer.music.set_volume(0)
                    constantes.MUSICA_PARTIDA = False
                else:
                    pygame.mixer.music.set_volume(0.05)
                    constantes.MUSICA_PARTIDA = True

def shoot(turno, tanques, terreno, game):
    # Se intancia el disparo
    disparo = Disparo(turno.tanque.angulo_n, turno.tanque.velocidad_disparo, turno.tanque, Bala(turno.tanque.tipo_bala))
    if turno.tanque.municion[turno.tanque.tipo_bala].unidades > 0:
        tanque_danyado = turno.tanque.disparar(pantalla=constantes.PANTALLA, terreno=terreno, ancho=constantes.ANCHO_VENTANA,
                                    alto=constantes.ALTO_VENTANA, disparo=disparo,
                                    altura_terreno=terreno.matriz, tanques=tanques)
        # Ningun tanque dañado
        if tanque_danyado != -1:
            if tanque_danyado.salud <= 0:
                if turno.tanque == tanque_danyado:
                    detectar_suicidio(turno)
                else:
                    constantes.TANQUES.remove(tanque_danyado)
                    detectar_kill(turno)
                    
            
        terreno.destruir_terreno(constantes.ALTO_VENTANA, constantes.ANCHO_VENTANA, disparo, disparo.proyectil)
            
        turno.tanque.municion[turno.tanque.tipo_bala].unidades -= 1
        turno.tanque.balas -= 1
        turno.puede_jugar = False
        cambiar_turno()
        return disparo
    else:
        return None


def detectar_suicidio(turno):
    turno.dinero -= 5000


def detectar_kill(turno):
    turno.kills += 1
    turno.dinero += 5000


def limpiar_constantes():
    constantes.JUGADORES = []
    constantes.TANQUES = []
    constantes.ARRAY_TURNOS = []
    constantes.EN_RONDA_DE_COMPRA = True
    constantes.RONDA_ACTUAL = 1
    constantes.TURNO_ACTUAL = 0

def vaciar_variables():
    limpiar_constantes()
    for jugador in constantes.JUGADORES:
        jugador.puede_jugar = False
        jugador.dinero = 10000
        jugador.kills = 0
        
        # Limpiar balas
        jugador.tanque.municion[0].unidades = 0
        jugador.tanque.municion[1].unidades = 0
        jugador.tanque.municion[2].unidades = 0
        jugador.tanque.balas = 0

def controles(event, teclas, turno, tanques, terreno, game):
    if teclas[pygame.K_a]:
        turno.tanque.angulo_n += 0.5
        if turno.tanque.angulo_n > constantes.LIMITE_ANGULO_MAX:
            turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MAX
        turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
    if teclas[pygame.K_a] and teclas[pygame.K_LSHIFT]:
        turno.tanque.angulo_n += 1.5
        if turno.tanque.angulo_n > constantes.LIMITE_ANGULO_MAX:
            turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MAX
        turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
    # Verifica si la tecla 'D' se mantiene presionada
    if teclas[pygame.K_d]:
        turno.tanque.angulo_n -= 0.5
        if turno.tanque.angulo_n < constantes.LIMITE_ANGULO_MIN:
            turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MIN
        turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
    if teclas[pygame.K_d] and teclas[pygame.K_LSHIFT]:
        turno.tanque.angulo_n -= 1.5
        if turno.tanque.angulo_n < constantes.LIMITE_ANGULO_MIN:
            turno.tanque.angulo_n = constantes.LIMITE_ANGULO_MIN
        turno.tanque.angulo_canon = math.radians(turno.tanque.angulo_n)
    # Verifica si la tecla 'W' se mantiene presionada
    if teclas[pygame.K_w]:
        turno.tanque.velocidad_disparo += 1.5
    if teclas[pygame.K_w] and teclas[pygame.K_LSHIFT]:
        turno.tanque.velocidad_disparo += 3.0
    # Verifica si la tecla 'S' se mantiene presionada
    if teclas[pygame.K_s]:
        turno.tanque.velocidad_disparo -= 1.5
        if turno.tanque.velocidad_disparo < constantes.LIMITE_VELOCIDAD_MIN:
            turno.tanque.velocidad_disparo = constantes.LIMITE_VELOCIDAD_MIN
    if teclas[pygame.K_s] and teclas[pygame.K_LSHIFT]:
        turno.tanque.velocidad_disparo -= 3.0
        if turno.tanque.velocidad_disparo < constantes.LIMITE_VELOCIDAD_MIN:
            turno.tanque.velocidad_disparo = constantes.LIMITE_VELOCIDAD_MIN
    # Cambio de tipo de municion al apretar la tecla 'Q' estas rotan en un ciclo
    if teclas[pygame.K_q]:
        if turno.tanque.tipo_bala < 2:
            turno.tanque.tipo_bala += 1
        else:
            turno.tanque.tipo_bala = 0

    # Verifica disparo del tanque y cambio de turnos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:  # Disparo
            constantes.DISPARO = shoot(turno, tanques, terreno, game)

def ui_pre_disparo(ui, pantalla, turno):
    ui.rectangulo(pantalla)
    ui.texto_jugador(pantalla, turno.tanque.color, turno.nombre)
    ui.texto_ajustes_disparo(pantalla)
    ui.texto_angulo(pantalla, turno.tanque.angulo_n)
    ui.texto_velocidad(pantalla, turno.tanque.velocidad_disparo)
    ui.texto_dinero(pantalla, turno.dinero)
    ui.texto_salud(pantalla, turno.tanque.salud)
    ui.texto_tipo_bala(pantalla, turno.tanque.tipo_bala)
    ui.cantidad_img_balas(pantalla, turno.tanque.tipo_bala, turno.tanque.municion[turno.tanque.tipo_bala].unidades)
    ui.ronda_actual(pantalla)
    ui.kills(pantalla, turno.kills)

def iniciar_tanques(terreno):
    for jugador in constantes.JUGADORES :
        jugador.tanque.posicion_y = calcular_y(terreno.matriz, jugador.tanque)
        jugador.tanque.caida_tanque = jugador.tanque.posicion_y

def controles_compra(self,turno):
    Compra.run(self,turno)

def combrobar_compra_de_todos_los_jugadores():
    if constantes.TURNO_ACTUAL >= constantes.NUM_JUGADORES:
        constantes.EN_RONDA_DE_COMPRA = False
        constantes.TURNO_ACTUAL = 0
        

def cambiar_musica(nueva_cancion):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(nueva_cancion)
    pygame.mixer.music.play()

def tanque_sin_municion(tanque_turno):
    if tanque_turno.balas <= 0:
        return True
    else:
        return False
    
def combrobar_municion_tanques():
    tanques_sin_municion = 0
    for tanque in constantes.TANQUES:
        if tanque_sin_municion(tanque):
            tanques_sin_municion += 1

    if tanques_sin_municion >= len(constantes.TANQUES) and constantes.EN_RONDA_DE_COMPRA == False:
        avanzar_partido()

def avanzar_partido():
    constantes.RONDA_ACTUAL += 1
    constantes.TURNO_ACTUAL = 0
    constantes.EN_RONDA_DE_COMPRA = True
    for jugador in constantes.JUGADORES:
        jugador.dinero += 10000
        jugador.tanque.salud = 100

    pos_inicial = 0
    pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.NUM_JUGADORES
    for jugador in constantes.JUGADORES:
        jugador.tanque.posicion_x = random.randint(pos_inicial, pos_final)
        jugador.tanque.posicion_y = 30
        jugador.tanque.angulo_canon = 0
        pos_inicial = pos_final
        pos_final = pos_inicial + constantes.ANCHO_VENTANA // constantes.NUM_JUGADORES

    altura_terreno = constantes.TERRENO.generar_terreno_perlin(constantes.DIMENSIONES[0])
    constantes.TERRENO.generar_matriz(constantes.ANCHO_VENTANA, constantes.ANCHO_VENTANA, altura_terreno)
    iniciar_tanques(constantes.TERRENO)

    definir_turnos()

def saltar_turno_tanque_sin_municion(turno):
    if tanque_sin_municion(turno.tanque):
        turno.puede_jugar = False
        cambiar_turno()


def queda_un_jugador_vivo():
    jugadores_vivos = 0
    for tanque in constantes.TANQUES:
        if tanque.salud > 0:
            jugadores_vivos += 1
    if jugadores_vivos == 1:
        return True
    else:
        return False
    
def comprobar_jugadores_vivos():
    if queda_un_jugador_vivo() and constantes.EN_RONDA_DE_COMPRA == False:
        avanzar_partido()

def verificar_termino_partida(game):
    if not constantes.RONDA_ACTUAL <= constantes.NUM_PARTIDAS:
        game.en_partida = False

def definir_ganador():
    max_kills = -1
    ganador_temp = None
    index_ganador = None
    for i in range(len(constantes.JUGADORES)):
        if constantes.JUGADORES[i].kills > max_kills:
            max_kills = constantes.JUGADORES[i].kills
            ganador_temp = constantes.JUGADORES[i]
            index_ganador = i
    
    empate = False
    for i in range(len(constantes.JUGADORES)):
        if i != index_ganador and constantes.JUGADORES[i].kills == max_kills:
            empate = True
            return empate

    if not empate:
        if ganador_temp is not None:
            return ganador_temp.nombre
    else:
        return -1
    

def actualizar_velocidad_viento():
    constantes.VELOCIDAD_VIENTO = random.randint(-30, 30)
    print(f"Velocidad Viento: {constantes.VELOCIDAD_VIENTO} m/s.")
