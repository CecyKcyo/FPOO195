from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox 
from ControladorUsuarios import Controlador
from PIL import Image, ImageTk

objControlador = Controlador()
# Función que se llamará al presionar el botón de guardar usuario.

def ejecutaActualizar():
    objControlador.actualizarUsuario(id_entry.get(), nombre_entry.get(), contraseña_entry.get(), departamento_entry.get())

      # Actualiza la lista de usuarios en la pestaña de consulta

def load_image(file_name, width, height):
    try:
        image = Image.open(file_name)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_name}'")


root = tk.Tk()
root.title("Editar Usuario")

# Marco principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Título
titulo_label = ttk.Label(main_frame, text="Editar Usuario", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

id_label = ttk.Label(main_frame, text="Ingresa el Id a editar:")
id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
id_entry = ttk.Entry(main_frame)
id_entry.grid(row=1, column=1, padx=5, pady=5)

# Texto e ingreso de Nombre
nombre_label = ttk.Label(main_frame, text="Nuevo nombre(s):")
nombre_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
nombre_entry = ttk.Entry(main_frame)
nombre_entry.grid(row=4, column=1, padx=5, pady=5)




# Texto e ingreso de Contraseña
contraseña_label = ttk.Label(main_frame, text="Contraseña:")
contraseña_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
contraseña_entry = ttk.Entry(main_frame)
contraseña_entry.grid(row=5, column=1, padx=5, pady=5)

# Texto e ingreso de departamento
departamento_label = ttk.Label(main_frame, text="departamento:")
departamento_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
departamento_entry = ttk.Entry(main_frame)
departamento_entry.grid(row=6, column=1, padx=5, pady=5)





# Botón "Guardar"
save_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/save.png", 20, 20) 
guardar_button = ttk.Button(main_frame, text="Guardar", image=save_image, compound=tk.LEFT, command=ejecutaActualizar)
guardar_button.grid(row=9, column=1, padx=5, pady=10, sticky="e")

root.mainloop()
