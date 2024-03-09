

import tkinter as tk
from tkinter import messagebox, font
import string
import random

# Definición de la clase PasswordGenerator
class generador:
    def __init__(self, tamaño=8, mayusculas=True, caracterEspecial=True):
        self.tamaño = tamaño
        self.mayusculas = mayusculas
        self.caracterEspecial = caracterEspecial

    def generar_contraseña(self):
        characters = string.ascii_lowercase
        if self.mayusculas:
            characters += string.ascii_uppercase
        if self.caracterEspecial:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.tamaño))
        return password

    def fortaleza(self, password):
        if len(password) < 12:
            return "Esta, tibia"
        elif not self.caracterEspecial:
            return "Medio chida"
        else:
            return "¡Fuerte como Gera!"

# Definición de la clase aplicacion
class aplicacion:
    def __init__(self, root, generador_contraseñas):
        self.root = root
        self.generador_contraseñas = generador_contraseñas
        self.setup_ui()

    def generar_contraseña_action(self):
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
        self.root.title("Generador de Contraseñas")

        # Colores en tonos rosas
        bg_color = "#ffeff1"
        text_color = "#d81b60"
        button_color = "#f06292"
        entry_bg_color = "#fce4ec"
        entry_fg_color = "#c2185b"
        self.root.configure(bg=bg_color)

        customFont = font.Font(family="Helvetica", size=10)

        tk.Label(self.root, text="Tamaño:", bg=bg_color, fg=text_color, font=customFont).grid(row=0, column=0, sticky="w")
        self.tamaño_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color, font=customFont)
        self.tamaño_entry.grid(row=0, column=1, sticky="ew")
        self.tamaño_entry.insert(0, "8")

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(self.root, text="Incluir mayúsculas", variable=self.uppercase_var, selectcolor=bg_color, bg=bg_color, fg=text_color, font=customFont)
        self.uppercase_checkbutton.grid(row=1, column=0, columnspan=2, sticky="w")
        self.uppercase_var.set(True)

        self.specialchar_var = tk.BooleanVar()
        self.specialchar_checkbutton = tk.Checkbutton(self.root, text="Incluir caracteres especiales", variable=self.specialchar_var, selectcolor=bg_color, bg=bg_color, fg=text_color, font=customFont)
        self.specialchar_checkbutton.grid(row=2, column=0, columnspan=2, sticky="w")
        self.specialchar_var.set(True)

        tk.Button(self.root, text="Generar contraseña", command=self.generar_contraseña_action, bg=button_color, fg=bg_color, font=customFont).grid(row=3, column=0, columnspan=2, pady=5)

        self.password_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color, font=customFont)
        self.password_entry.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        self.root.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = aplicacion(root, generador())
    root.mainloop()
