from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox 
# Importamos el controlador de productos en lugar del de usuarios
from ControladorAgregarProducto import Controlador
from PIL import Image, ImageTk

objControlador = Controlador()

# Función que se llamará al presionar el botón de guardar producto.
def ejecutaInsert():
    # Adaptamos la función para tomar los campos de la tabla productos
    objControlador.insertProducto(nombre_entry.get(), cantidad_entry.get(), precio_entry.get())

# Cargamos la imagen como antes, esta función no necesita cambios
def load_image(file_name, width, height):
    try:
        image = Image.open(file_name)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_name}'")

root = tk.Tk()
root.title("Agregar Producto")

# Marco principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Título
titulo_label = ttk.Label(main_frame, text="Agregar Producto", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Texto e ingreso de Nombre de Producto
nombre_label = ttk.Label(main_frame, text="Nombre del Producto:")
nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
nombre_entry = ttk.Entry(main_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)

# Texto e ingreso de Cantidad
cantidad_label = ttk.Label(main_frame, text="Cantidad:")
cantidad_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
cantidad_entry = ttk.Entry(main_frame)
cantidad_entry.grid(row=2, column=1, padx=5, pady=5)

# Texto e ingreso de Precio
precio_label = ttk.Label(main_frame, text="Precio:")
precio_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
precio_entry = ttk.Entry(main_frame)
precio_entry.grid(row=3, column=1, padx=5, pady=5)

# Botón "Guardar"
save_image = load_image("save.png", 20, 20) # Asumiendo que la imagen está en el mismo directorio
guardar_button = ttk.Button(main_frame, text="Guardar", image=save_image, compound=tk.LEFT, command=ejecutaInsert)
guardar_button.grid(row=4, column=1, padx=5, pady=10, sticky="e")

root.mainloop()
