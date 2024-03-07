import tkinter as tk
from tkinter import messagebox
from crud import CRUD

class AplicacionLogin:
    def __init__(self, gestor_usuarios):
        self.ventana = tk.Tk()
        self.ventana.title("Login")

        self.gestor_usuarios = gestor_usuarios

        tk.Label(self.ventana, text="Correo:").grid(row=0, column=0)
        self.entrada_correo = tk.Entry(self.ventana)
        self.entrada_correo.grid(row=0, column=1)

        tk.Label(self.ventana, text="Contraseña:").grid(row=1, column=0)
        self.entrada_contraseña = tk.Entry(self.ventana, show="*")
        self.entrada_contraseña.grid(row=1, column=1)

        tk.Button(self.ventana, text="Iniciar Sesión", command=self.validar_credenciales).grid(row=2, column=0, columnspan=2)

    def iniciar(self):
        self.ventana.mainloop()

    def validar_credenciales(self):
        correo = self.entrada_correo.get()
        contraseña = self.entrada_contraseña.get()

        if not correo or not contraseña:
            messagebox.showwarning("Campos vacíos", "Por favor, ingrese su correo y contraseña")
            return

        usuario = self.gestor_usuarios.buscar_usuario_por_correo(correo)
        if usuario and usuario.obtener_contraseña() == contraseña:
            messagebox.showinfo("Login exitoso", "Bienvenido al sistema")
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos. Por favor, revise sus datos")
