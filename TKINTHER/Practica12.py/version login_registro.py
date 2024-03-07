import tkinter as tk
from tkinter import messagebox, simpledialog
from crud import CRUD
from usuario import Usuario

class Aplicacion:
    def __init__(self):
        self.gestor_usuarios = CRUD()
        self.root = tk.Tk()
        self.root.title('Sistema de Login y Gestión de Usuarios')

        # Botón para el Login
        tk.Button(self.root, text="Login", command=self.mostrar_login).pack(pady=10)

        # Botón para agregar un nuevo usuario
        tk.Button(self.root, text="Registrar Usuario", command=self.registrar_usuario).pack(pady=10)

    def mostrar_login(self):
        login_ventana = tk.Toplevel(self.root)
        login_ventana.title('Login')

        tk.Label(login_ventana, text="Correo:").grid(row=0, column=0)
        entrada_correo = tk.Entry(login_ventana)
        entrada_correo.grid(row=0, column=1)

        tk.Label(login_ventana, text="Contraseña:").grid(row=1, column=0)
        entrada_contraseña = tk.Entry(login_ventana, show="*")
        entrada_contraseña.grid(row=1, column=1)

        def validar_credenciales():
            correo = entrada_correo.get()
            contraseña = entrada_contraseña.get()

            if not correo or not contraseña:
                messagebox.showwarning("Campos vacíos", "Por favor, ingrese su correo y contraseña")
            elif self.gestor_usuarios.buscar_usuario_por_correo(correo, contraseña):
                messagebox.showinfo("Login exitoso", "Bienvenido al sistema")
                login_ventana.destroy()
            else:
                messagebox.showerror("Error", "Correo o contraseña incorrectos. Por favor, revise sus datos")

        tk.Button(login_ventana, text="Login", command=validar_credenciales).grid(row=2, column=0, columnspan=2)

    def registrar_usuario(self):
        id_usuario = simpledialog.askstring("Registro", "Ingrese ID del usuario:")
        correo = simpledialog.askstring("Registro", "Ingrese correo del usuario:")
        contraseña = simpledialog.askstring("Registro", "Ingrese contraseña del usuario:")

        if not id_usuario or not correo or not contraseña:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        usuario = Usuario(int(id_usuario), contraseña, correo)
        self.gestor_usuarios.crear_usuario(usuario)
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()
