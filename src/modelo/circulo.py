import math
from modelo.punto import Punto
class Circulo:

    def __init__(self, centro:Punto, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * (self.radio)**2
    
    def perimetro(self):
        return 2*math.pi*self.radio
    
    def dentro_del_circulo(self, punto:Punto):
        return self.radio > self.centro.calcular_distancia(punto)