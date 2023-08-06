import math
class Punto:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def mostrar(self):
        print("la coordenada x es ", self.x)
        print("la coordenada y es ", self.y)

    def mover(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def calcular_distancia(self, punto_b):
        distancia = math.sqrt((punto_b.x -self.x)**2 + (punto_b.y - self.y)**2)
        return distancia