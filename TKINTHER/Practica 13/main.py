import tkinter as tk
from password_classes import generador, aplicacion

# Creación y ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    generar_contraseña = generador()
    app = aplicacion(root, generar_contraseña)
    root.mainloop()
