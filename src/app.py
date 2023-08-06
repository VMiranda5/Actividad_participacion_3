"""
from modelo.cuenta_bancaria import CuentaBancaria

mi_cuenta = CuentaBancaria('34423321', 'someone', 1000)
mi_cuenta.depositar(500)
print("ahora tengo ", mi_cuenta.balance)
mi_cuenta.retirar(300)
print("me quedaron ", mi_cuenta.balance)
mi_cuenta.aplicar_cuota_manejo()
print("al pagar cuota de manejo ", mi_cuenta.balance)
mi_cuenta.mostrar_detalles()
"""
"""
from modelo.circulo import Circulo
from modelo.punto import Punto
import math

circulo = Circulo(Punto(0,0),4)
punto = Punto(2, math.sqrt(12))

print("el perimetro es: ", circulo.perimetro())
print("el area es: ", circulo.area())
print("el punto esta dentro del circulo?", circulo.dentro_del_circulo(punto))
"""
"""
from modelo.rectangulo import Rectangulo
from modelo.punto import Punto
rectangulo = Rectangulo(Punto(3,1), Punto(6,4))

print("el perimetro es:", rectangulo.perimetro())

print("el area es: ", rectangulo.area())

print("es cuadrado? ", rectangulo.es_cuadrado())
"""
"""
from modelo.punto import Punto

punto_1 = Punto(0,0)
punto_2 = Punto(4,3)
punto_2.mostrar()
punto_2.mover(1,2)
punto_2.mostrar()
print(punto_1.calcular_distancia(punto_2))
"""