from modelo.punto import Punto

class Rectangulo:

    def __init__(self, esquina_1:Punto, esquina_2:Punto):
        self.esquina_1 = esquina_1
        self.esquina_2 = esquina_2

    def perimetro(self):
        p = 2*(abs(self.esquina_1.x-self.esquina_2.x)+abs(self.esquina_1.y-self.esquina_2.y))
        return p
    
    def area(self):
        a = abs(self.esquina_1.x-self.esquina_2.x)*abs(self.esquina_1.y-self.esquina_2.y)
        return a
    
    def es_cuadrado(self):
        return abs(self.esquina_1.x-self.esquina_2.x) == abs(self.esquina_1.y-self.esquina_2.y)