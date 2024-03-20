class Cuenta:
    def __init__(self, numero_cuenta, titular, edad, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def titular(self):
        return self.__titular

    @property
    def edad(self):
        return self.__edad

    @property
    def saldo(self):
        return self.__saldo
