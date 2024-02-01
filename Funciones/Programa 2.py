'''Escribir una función que calcule el área de un círculo y otra que
calcule el volumen de un cilindro usando la primera función.'''
import math

def area(radio):
    return math.pi*radio**2
def volumen(radio, altura):
    return area(radio)*altura

radio=float(input("Ingrese el radio del circulo:"))
altura=float(input("Ingrese la altura del cilindro:"))
areav=area(radio)
c_volumen=volumen(radio, altura)
print("El area del circulo es:", areav)
print("El volumen del cilindro es:", c_volumen)



