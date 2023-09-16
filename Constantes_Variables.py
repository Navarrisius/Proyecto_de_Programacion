from clases import *
#Constantes
ANCHO_VENTANA = 1280
ALTO_VENTANA = 768
NOMBRE_VENTANA = "Juego XD"
limite_angulo_min = 0
limite_angulo_max = 180
gravedad = 1

#Colores

#  ----------------Seting tanque-------------
#Jugador 1
jugador_1 = Jugador(None, Tanque("red"))
jugador_1.tanque.posicion_x = 30
jugador_1.tanque.posicion_y = 30
jugador_1.tanque.angulo_n = 0
jugador_1.puede_jugar = False
jugador_1.tanque.angulo_canon = (math.radians(jugador_1.tanque.angulo_n))

#Jugador 2
jugador_2 = Jugador(None, Tanque("blue"))
jugador_2.tanque.posicion_x = 200*4
jugador_2.tanque.posicion_y = 30
jugador_2.tanque.angulo_n = 0
jugador_2.tanque.angulo_canon = (math.radians(jugador_2.tanque.angulo_n))
jugador_2.puede_jugar = True
