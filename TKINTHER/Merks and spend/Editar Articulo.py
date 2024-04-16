from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ControladorAgregarProducto import Controlador  # Asegúrate de tener este controlador con métodos para productos
from PIL import Image, ImageTk

objControlador = Controlador()

def solo_numeros(char):
    return char.isdigit()

def solo_letras(char):
    return char.isalpha() or char.isspace()

def confirmar_y_actualizar():
    # Recuperamos los valores actuales de los campos de entrada
    id_producto = id_entry.get()
    nombre_producto = nombre_entry.get()
    cantidad_producto = cantidad_entry.get()
    precio_producto = precio_entry.get()
    
    # Mostramos un cuadro de diálogo para confirmar la actualización
    if messagebox.askyesno("Confirmar Actualización", f"Estás a punto de actualizar el producto con los siguientes datos:\n\n"
                                                       f"ID: {id_producto}\n"
                                                       f"Nombre: {nombre_producto}\n"
                                                       f"Cantidad: {cantidad_producto}\n"
                                                       f"Precio: ${precio_producto}\n\n"
                                                       "¿Deseas proceder?"):
        ejecutaActualizar()

def ejecutaActualizar():
    # Realizar la actualización aquí
    actualizado = objControlador.actualizarProducto(id_entry.get(), nombre_entry.get(), cantidad_entry.get(), precio_entry.get())
    if actualizado:
        messagebox.showinfo("Actualización Exitosa", "El producto ha sido actualizado exitosamente.")
        root.destroy()  # Cierra la ventana principal si la actualización fue exitosa
    else:
        messagebox.showerror("Error de Actualización", "No se pudo actualizar el producto.")


def load_image(file_name, width, height):
    try:
        image = Image.open(file_name)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_name}'")

root = tk.Tk()
root.title("Editar Producto")

# Marco principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Título
titulo_label = ttk.Label(main_frame, text="Editar Producto", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

validate_number = (root.register(solo_numeros), '%S')
validate_text = (root.register(solo_letras), '%S')

# Texto e ingreso de ID
id_label = ttk.Label(main_frame, text="ID del Producto:")
id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
id_entry = ttk.Entry(main_frame, validate='key', validatecommand=validate_number)
id_entry.grid(row=1, column=1, padx=5, pady=5)

# Texto e ingreso de Nombre del Producto
nombre_label = ttk.Label(main_frame, text="Nombre del Producto:")
nombre_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
nombre_entry = ttk.Entry(main_frame, validate='key', validatecommand=validate_text)
nombre_entry.grid(row=2, column=1, padx=5, pady=5)

# Texto e ingreso de Cantidad
cantidad_label = ttk.Label(main_frame, text="Cantidad:")
cantidad_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
cantidad_entry = ttk.Entry(main_frame, validate='key', validatecommand=validate_number)
cantidad_entry.grid(row=3, column=1, padx=5, pady=5)

# Texto e ingreso de Precio
precio_label = ttk.Label(main_frame, text="Precio:$")
precio_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
precio_entry = ttk.Entry(main_frame, validate='key', validatecommand=validate_number)
precio_entry.grid(row=4, column=1, padx=5, pady=5)

# Botón "Guardar"
save_image = load_image("save.png", 20, 20)  # Asumiendo que la imagen está en el mismo directorio
guardar_button = ttk.Button(main_frame, text="Guardar", image=save_image, compound=tk.LEFT, command=confirmar_y_actualizar)
guardar_button.grid(row=5, column=1, padx=5, pady=10, sticky="e")

root.mainloop()
