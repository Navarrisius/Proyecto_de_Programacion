from configuraciones import Configuracion


NOMBRE_VENTANA = "PessiTank"
LIMITE_ANGULO_MIN = 0
LIMITE_ANGULO_MAX = 180
LIMITE_VELOCIDAD_MIN = 30
GRAVEDAD = 9.8
ANCHO_VENTANA = 800
ALTO_VENTANA = 800
JUGADORES = []
TANQUES = []
CANT_JUGADORES = 2
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
PLOMO = (155, 155, 155)
CELESTE = (114,158,188)
DISPARO = None
PANTALLA = None
num_jugadores = 2
num_partidos = 1
efectos_entorno = True
dimenciones = [1920, 1080]
config_defecto = Configuracion(2,800,800,1)
config_maximas = Configuracion(6,1920,1080,20)
MUSICA_PARTIDA = True

'''
HitBox del tanque:
x_izq = -40
x_der = 30
y_arriba = -30
y_abajo = 12
'''