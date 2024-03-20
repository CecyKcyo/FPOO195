from Cuenta import Cuenta

class ManejoCuentas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                self.cuentas.remove(cuenta)
                return True
        return False

    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None
