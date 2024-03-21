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
    
    def retirar_efectivo(self, cantidad):
        # """Intenta retirar una cantidad de dinero de la cuenta.
        
        # Args:
        #     cantidad (float): La cantidad de dinero a retirar.
        
        # Returns:
        #     bool: True si el retiro fue exitoso, False si no hay saldo suficiente.
        # """
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
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
