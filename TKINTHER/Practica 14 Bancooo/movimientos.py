class Movimientos:
    def __init__(self, elquemanejalascuentas):
        self.elquemanejalascuentas = elquemanejalascuentas

    def depositar(self, numero_cuenta, cantidad):
        cuenta = self.elquemanejalascuentas.buscar_cuenta(numero_cuenta)
        if cuenta and cantidad > 0:
            cuenta.ingresar(cantidad)
            return True
        return False

    def transferir(self, cuenta_origen, cuenta_destino, cantidad):
        origen = self.elquemanejalascuentas.buscar_cuenta(cuenta_origen)
        destino = self.elquemanejalascuentas.buscar_cuenta(cuenta_destino)
        if origen and destino and cantidad > 0 and origen.retirar(cantidad):
            destino.ingresar(cantidad)
            return True
        return False

    def retirar(self, numero_cuenta, cantidad):
        cuenta = self.elquemanejalascuentas.buscar_cuenta(numero_cuenta)
        if cuenta and cantidad > 0 and cuenta.retirar(cantidad):
            return True
        return False
