class Movimientos:
    def __init__(self, manejador_cuentas):
        self.manejador_cuentas = manejador_cuentas

    def depositar(self, numero_cuenta, cantidad):
        cuenta = self.manejador_cuentas.buscar_cuenta(numero_cuenta)
        if cuenta and cantidad > 0:
            cuenta.ingresar(cantidad)
            return True
        return False

    def transferir(self, numero_cuenta_origen, numero_cuenta_destino, cantidad):
        cuenta_origen = self.manejador_cuentas.buscar_cuenta(numero_cuenta_origen)
        cuenta_destino = self.manejador_cuentas.buscar_cuenta(numero_cuenta_destino)
        if cuenta_origen and cuenta_destino and cantidad > 0:
            if cuenta_origen.saldo >= cantidad:
                cuenta_origen.retirar(cantidad)
                cuenta_destino.ingresar(cantidad)
                return True
            else:
                return False
        return False
