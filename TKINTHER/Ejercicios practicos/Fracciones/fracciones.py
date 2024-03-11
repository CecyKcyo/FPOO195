# fracciones.py

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.reducir()

    def reducir(self):
        divisor = mcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __sub__(self, otra):
        nuevo_numerador = self.numerador * otra.denominador - otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, otra):
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, otra):
        nuevo_numerador = self.numerador * otra.denominador
        nuevo_denominador = self.denominador * otra.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)
