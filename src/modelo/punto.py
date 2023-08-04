class Punto:

    def __init__(self):

        self.x = 0
        self.y = 0

    def mostrar(self):
        print("la coordenada x es ", self.x)
        print("la coordenada y es ", self.y)

    def mover(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def calcular_distancia(self)#????