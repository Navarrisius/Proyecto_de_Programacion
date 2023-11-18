import random, constantes, pygame

class Terreno:
    def __init__(self):
        self.constante_oscilacion = random.uniform(0.01, 0.0135)
        self.matriz = []
        self.arreglo = []
        self.tipo = random.randint(1,3)


    def generar_terreno_perlin(self, rango_onda):
        if rango_onda == 800:
            onda = 0.012
        else:
            onda = 0.006
        gradientes = [random.uniform(-1, 1) for _ in range(256)]
        #Funcion para la atenuacion
        def fade(t):
            return (t**3) * (t * (t * 6 - 15) + 10)
        #Funcion basica para ruido de perlin
        def perlin(x):
            X = int(x) & 255
            x -= int(x)
            u = fade(x)
            a = gradientes[X]
            b = gradientes[X + 1]
            val1 = a * x
            val2 = b * (x - 1)
            return (1 - u) * val1 + u * val2
        arr = []
        for x in range(constantes.ANCHO_VENTANA):
            arr.append(int(constantes.ALTO_VENTANA / 2 + perlin(x * onda) * 600))
        return arr


    def dibujar_terreno(self, pantalla):
        for pos in range(len(self.arreglo)):
            if pos % 2 == 0:
                pygame.draw.line(pantalla, (173, 204, 246), self.arreglo[pos], self.arreglo[pos + 1])


    def generar_matriz(self, ancho_ventana, alto_ventana, arreglo_terreno):
        self.matriz = [['x' if x >= arreglo_terreno[y] else 'o' for y in range(ancho_ventana)] for x in range(alto_ventana)]
        self.generar_arreglo_m()


    def destruir_terreno(self, alto, ancho, bala, municion):
        impacto_x = int(bala.eje_x[-1])
        impacto_y = int(bala.eje_y[-1])

        radio = municion.radio_impacto
        
        for y in range(max(0, impacto_y - radio), min(alto, impacto_y + radio)):
            for x in range(max(0, impacto_x - radio), min(ancho, impacto_x + radio)):
                distancia = ((x - impacto_x) ** 2 + (y - impacto_y) ** 2) ** 0.5
                if distancia <= radio:
                    self.matriz[y][x] = "o"

        self.generar_arreglo_m()
        

    def generar_arreglo_m(self):
        self.arreglo = []
        for y in range(len(self.matriz[0])):
            x = 0
            while x < len(self.matriz):
                if self.matriz[x][y] == 'x':
                    pos_inicial = (y, x)
                    while x < len(self.matriz) and self.matriz[x][y] == 'x':
                        x += 1
                    pos_final = (y, x - 1)
                    self.arreglo.extend((pos_inicial, pos_final))
                x += 1