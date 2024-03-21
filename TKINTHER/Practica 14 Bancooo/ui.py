import tkinter as tk
from tkinter import messagebox
from manejo_cuentas import ManejoCuentas  
from movimientos import Movimientos  
from Cuenta import Cuenta  

class VentanaMovimientos(tk.Toplevel):
    def __init__(self, parent, manejador_cuentas):
        super().__init__(parent)
        self.manejador_cuentas = manejador_cuentas
        self.movimientos = Movimientos(self.manejador_cuentas)
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
