from Configuracion import Configuracion


NOMBRE_VENTANA = "PessiTank"
LIMITE_ANGULO_MIN = 0
LIMITE_ANGULO_MAX = 180
LIMITE_VELOCIDAD_MIN = 30
GRAVEDAD = 0.5
ANCHO_VENTANA = 800
ALTO_VENTANA = 800
JUGADORES = []
TANQUES = []
ARRAY_TURNOS = []
JUGADOR_IMPACTADO = None
TURNO_ACTUAL = 0
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
PLOMO = (155, 155, 155)
CELESTE = (114,158,188)
DISPARO = None
PANTALLA = None
NUM_JUGADORES = 2
NUM_PARTIDAS = 1
EFECTOS_ENTORNO = True
DIMENSIONES = [1920, 1080]
config_defecto = Configuracion(2,800,800,1)
config_maximas = Configuracion(6,1920,1080,20)
MUSICA_PARTIDA = True
EN_RONDA_DE_COMPRA = True
MUSICA = None
RONDA_ACTUAL = 1
TERRENO = None

'''
HitBox del tanque:
x_izq = -40
x_der = 30
y_arriba = -30
y_abajo = 12
'''