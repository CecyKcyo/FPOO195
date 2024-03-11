import tkinter as tk
from tkinter import messagebox, font
import string
import random

# Clase que define el comportamiento del generador de contraseñas
class generador:
    def __init__(self, tamaño=8, mayusculas=True, caracterEspecial=True):
        # Inicializa con las configuraciones básicas para generar una contraseña
        self.tamaño = tamaño
        self.mayusculas = mayusculas
        self.caracterEspecial = caracterEspecial

    def generar_contraseña(self):
        # Base de caracteres: siempre incluye minúsculas
        characters = string.ascii_lowercase
        # Añade mayúsculas si se especificó
        if self.mayusculas:
            characters += string.ascii_uppercase
        # Añade caracteres especiales si se especificó
        if self.caracterEspecial:
            characters += string.punctuation

        # Genera la contraseña seleccionando caracteres al azar de la cadena de caracteres permitidos
        password = ''.join(random.choice(characters) for _ in range(self.tamaño))
        return password

    def fortaleza(self, password):
        # Evalúa la fortaleza de la contraseña generada
        if len(password) < 12:
            return "Esta, tibia"
        elif not self.caracterEspecial :
            return "Medio tibia"
        else:
            return "¡Fuerte como Gera!"

# Clase que maneja la interfaz de usuario de la aplicación
class aplicacion:
    def __init__(self, root, generador_contraseñas):
        self.root = root  # Ventana principal de Tkinter
        self.generador_contraseñas = generador_contraseñas  # Instancia del generador de contraseñas
        self.setup_ui()  # Configura la interfaz de usuario al inicializar

    def generar_contraseña_action(self):
        # Obtiene las preferencias del usuario desde la interfaz y genera una contraseña
        tamaño = int(self.tamaño_entry.get())
        mayusculas = self.uppercase_var.get()
        caracterEspecial = self.specialchar_var.get()
        self.generador_contraseñas.tamaño = tamaño
        self.generador_contraseñas.mayusculas = mayusculas
        self.generador_contraseñas.caracterEspecial = caracterEspecial
        password = self.generador_contraseñas.generar_contraseña()
        fortaleza = self.generador_contraseñas.fortaleza(password)
        messagebox.showinfo("Generador de contras", f"Contraseña: {password}\nFortaleza: {fortaleza}")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def setup_ui(self):
        # Configura elementos de la interfaz de usuario como etiquetas, campos de entrada, botones, etc.
        self.root.title("Generador de Contraseñas")
        # Define colores y estilos
        bg_color = "#ffeff1"
        text_color = "#d81b60"
        button_color = "#f06292"
        entry_bg_color = "#fce4ec"
        entry_fg_color = "#c2185b"
        self.root.configure(bg=bg_color)

        customFont = font.Font(family="Helvetica", size=10)

        # Configuración de widgets (etiquetas, entradas, botones de verificación, botón de acción)
        tk.Label(self.root, text="Tamaño:", bg=bg_color, fg=text_color, font=customFont).grid(row=0, column=0, sticky="w")
        self.tamaño_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color, font=customFont)
        self.tamaño_entry.grid(row=0, column=1, sticky="ew")
        self.tamaño_entry.insert(0, "8")  # Valor predeterminado para el tamaño

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(self.root, text="Incluir mayúsculas", variable=self.uppercase_var, selectcolor=bg_color, bg=bg_color, fg=text_color, font=customFont)
        self.uppercase_checkbutton.grid(row=1, column=0, columnspan=2, sticky="w")
        self.uppercase_var.set(True)  # Valor predeterminado para incluir mayúsculas

        self.specialchar_var = tk.BooleanVar()
        self.specialchar_checkbutton = tk.Checkbutton(self.root, text="Incluir caracteres especiales", variable=self.specialchar_var, selectcolor=bg_color, bg=bg_color, fg=text_color, font=customFont)
        self.specialchar_checkbutton.grid(row=2, column=0, columnspan=2, sticky="w")
        self.specialchar_var.set(True)  # Valor predeterminado para incluir caracteres especiales

        tk.Button(self.root, text="Generar contraseña", command=self.generar_contraseña_action, bg=button_color, fg=bg_color, font=customFont).grid(row=3, column=0, columnspan=2, pady=5)

        self.password_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color, font=customFont)
        self.password_entry.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Asegura que la segunda columna de la grilla se expanda con la ventana
        self.root.grid_columnconfigure(1, weight=1)

# Código para ejecutar si este archivo es el script principal
if __name__ == "__main__":
    root = tk.Tk()
    app = aplicacion(root, generador())  # Crea una instancia de la aplicación
    root.mainloop()  # Inicia el
