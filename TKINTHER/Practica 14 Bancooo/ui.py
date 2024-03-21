import tkinter as tk
from tkinter import messagebox
from manejo_cuentas import ManejoCuentas  
from movimientos import Movimientos  
from Cuenta import Cuenta  

class VentanaMovimientos(tk.Toplevel):
    def __init__(self, parent, elquemanejalascuentas):
        super().__init__(parent)
        self.elquemanejalascuentas = elquemanejalascuentas
        self.movimientos = Movimientos(self.elquemanejalascuentas)
        self.title("Movimientos de la Cuenta")
        self.geometry("400x500")
        self.configure(bg='light green')

        # Componentes UI para Depósito
        self.setup_deposito_seccion()

        # Componentes UI para Transferencia
        self.setup_transferencia_seccion()

        # Componentes UI para Retiro
        self.setup_retiro_seccion()

    def setup_deposito_seccion(self):
        tk.Label(self, text="Depositar a Cuenta", bg='light green').pack(pady=(10,0))
        
        tk.Label(self, text="Número de Cuenta:", bg='light green').pack()
        self.numero_cuenta_entry_mov = tk.Entry(self)
        self.numero_cuenta_entry_mov.pack()

        tk.Label(self, text="Cantidad a depositar:", bg='light green').pack()
        self.cantidad_deposito_entry = tk.Entry(self)
        self.cantidad_deposito_entry.pack()

        tk.Button(self, text="Depositar", command=self.depositar, bg='green').pack(pady=5)

    def setup_transferencia_seccion(self):
        tk.Label(self, text="Transferir de una Cuenta a Otra", bg='light green').pack(pady=(20,0))
        
        tk.Label(self, text="Cuenta Origen:", bg='light green').pack()
        self.cuenta_origen_entry = tk.Entry(self)
        self.cuenta_origen_entry.pack()

        tk.Label(self, text="Cuenta Destino:", bg='light green').pack()
        self.cuenta_destino_entry = tk.Entry(self)
        self.cuenta_destino_entry.pack()

        tk.Label(self, text="Cantidad a transferir:", bg='light green').pack()
        self.cantidad_transferencia_entry = tk.Entry(self)
        self.cantidad_transferencia_entry.pack()

        tk.Button(self, text="Transferir", command=self.transferir, bg='green').pack(pady=5)

    def setup_retiro_seccion(self):
        tk.Label(self, text="Retirar de Cuenta", bg='light green').pack(pady=(20,0))

        tk.Label(self, text="Número de Cuenta para Retiro:", bg='light green').pack()
        self.numero_cuenta_retiro_entry = tk.Entry(self)
        self.numero_cuenta_retiro_entry.pack()

        tk.Label(self, text="Cantidad a retirar:", bg='light green').pack()
        self.cantidad_retiro_entry = tk.Entry(self)
        self.cantidad_retiro_entry.pack()

        tk.Button(self, text="Retirar", command=self.retirar, bg='green').pack(pady=5)

    def depositar(self):
        numero_cuenta = self.numero_cuenta_entry_mov.get()
        try:
            cantidad = float(self.cantidad_deposito_entry.get())
            if self.movimientos.depositar(numero_cuenta, cantidad):
                messagebox.showinfo("Éxito", "Depósito realizado con éxito")
            else:
                messagebox.showerror("Error", "No se pudo realizar el depósito")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")

    def transferir(self):
        cuenta_origen = self.cuenta_origen_entry.get()
        cuenta_destino = self.cuenta_destino_entry.get()
        try:
            cantidad = float(self.cantidad_transferencia_entry.get())
            if self.movimientos.transferir(cuenta_origen, cuenta_destino, cantidad):
                messagebox.showinfo("Éxito", "Transferencia realizada con éxito")
            else:
                messagebox.showerror("Error", "No se pudo realizar la transferencia")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")

    def retirar(self):
        numero_cuenta = self.numero_cuenta_retiro_entry.get()
        try:
            cantidad = float(self.cantidad_retiro_entry.get())
            if self.movimientos.retirar(numero_cuenta, cantidad):
                messagebox.showinfo("Éxito", "Retiro realizado con éxito")
            else:
                messagebox.showerror("Error", "No se pudo realizar el retiro o saldo insuficiente")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Cuentas de Caja Popular")
        self.manejo_cuentas = ManejoCuentas()
        self.geometry("400x300")
        self.configure(bg='pink')

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Gestión de Cuentas", bg='pink').pack(pady=10)
        tk.Label(self, text="Número de Cuenta:", bg='pink').pack()
        self.numero_cuenta_entry = tk.Entry(self)
        self.numero_cuenta_entry.pack()

        tk.Label(self, text="Titular:", bg='pink').pack()
        self.titular_entry = tk.Entry(self)
        self.titular_entry.pack()

        tk.Label(self, text="Edad:", bg='pink').pack()
        self.edad_entry = tk.Entry(self)
        self.edad_entry.pack()

        tk.Button(self, text="Agregar Cuenta", command=self.agregar_cuenta, bg='light pink').pack(pady=5)
        tk.Button(self, text="Consultar Saldo", command=self.consultar_saldo, bg='light pink').pack(pady=5)
        tk.Button(self, text="Movimientos de la Cuenta", command=self.abrir_ventana_movimientos, bg='light pink').pack(pady=5)

    def agregar_cuenta(self):
        numero_cuenta = self.numero_cuenta_entry.get()
        titular = self.titular_entry.get()
        try:
            edad = int(self.edad_entry.get())
            cuenta_nueva = Cuenta(numero_cuenta, titular, edad)
            self.manejo_cuentas.agregar_cuenta(cuenta_nueva)
            messagebox.showinfo("Éxito", "Cuenta agregada correctamente")
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero")

    def consultar_saldo(self):
        numero_cuenta = self.numero_cuenta_entry.get()
        cuenta = self.manejo_cuentas.buscar_cuenta(numero_cuenta)
        if cuenta:
            messagebox.showinfo("Saldo", f"El saldo de la cuenta {numero_cuenta} es: {cuenta.consultar_saldo()}")
        else:
            messagebox.showerror("Error", "Cuenta no encontrada")

    def abrir_ventana_movimientos(self):
        numero_cuenta = self.numero_cuenta_entry.get()
        if numero_cuenta:
            cuenta = self.manejo_cuentas.buscar_cuenta(numero_cuenta)
            if cuenta:
                VentanaMovimientos(self, self.manejo_cuentas)
            else:
                messagebox.showerror("Error", "Cuenta no encontrada")
        else:
            messagebox.showerror("Error", "Por favor, ingrese un número de cuenta")

if __name__ == "__main__":
    app = App()
    app.mainloop()
