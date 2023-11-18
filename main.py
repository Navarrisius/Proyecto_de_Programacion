import pygame
import constantes
import funciones
import sys
from gameStateManager import GameStateManager
from juego import EnPartida
from Menu import Menu
from Tutorial import Tutorial
from Configurar import Configurar
from Pausa import Pausa
from Termino import Termino
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('mp3/aria_math.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        img_ventana = pygame.image.load('img/pessi.png')
        pygame.display.set_icon(img_ventana)
        pygame.display.set_caption(constantes.NOMBRE_VENTANA)
        funciones.actualizar_info_pantalla()
        constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA = 1920, 1080
        self.reloj = pygame.time.Clock()
        constantes.PANTALLA = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.RESIZABLE, pygame.OPENGL)
        self.pantalla = constantes.PANTALLA
        self.game = funciones.Partida()
        self.gameStateManager = GameStateManager('menu')
        self.Menu = Menu(self.pantalla,self.gameStateManager,self.game)
        self.Tutorial = Tutorial(self.pantalla,self.gameStateManager,self.game)
        self.Partida = EnPartida(self.pantalla,self.gameStateManager,self.game)
        self.Configurar = Configurar(self.pantalla,self.gameStateManager,self.game)
        self.Pausar = Pausa(self.pantalla,self.gameStateManager,self.game)
        self.Termino = Termino(self.pantalla,self.gameStateManager,self.game)

        self.estados = {'menu':self.Menu,'tutorial':self.Tutorial,'partida':self.Partida,'configurar':self.Configurar,'pausar':self.Pausar,'termino':self.Termino}
    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.estados[self.gameStateManager.get_estado()].run()
            pygame.display.update()
            self.reloj.tick(60)


if __name__ == '__main__':
    juego = Game()
    juego.run()