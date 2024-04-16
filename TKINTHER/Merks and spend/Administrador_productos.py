import tkinter as tk
from tkinter import simpledialog
import subprocess

# Funciones para los botones
def abrir_editar_productos():
    # Aquí ejecutamos el archivo Python en una nueva ventana
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Editar Articulo.py'])
def agregar_productos():
    # Aquí ejecutamos el archivo Python en una nueva ventana
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Agregar articulo.py'])

def eliminar():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Eliminar Articulo.py'])
def consultar_productos():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Consultar productos.py'])
def consultar_productos():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Consultar productos.py'])

def generar_reportes():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Reporteproductos.py'])

# Crear la ventana principal
root = tk.Tk()
root.title("productos")

# Diseño minimalista: colores y fuente
background_color = "#ffffff"
button_color = "#f0f0f0"
text_color = "#333333"
font = ("Arial", 12)

# Aplicar colores de fondo y de fuente
root.configure(bg=background_color)

# Crear el título "productos"
lbl_titulo = tk.Label(root, text="productos", font=("Arial", 18), bg=background_color, fg=text_color)
lbl_titulo.pack(pady=10)

# Crear el marco principal
main_frame = tk.Frame(root, bg=background_color)
main_frame.pack(padx=20, pady=20)

# Crear los botones con un diseño minimalista
btn_editar = tk.Button(main_frame, text="Agregar", command=agregar_productos, bg=button_color, fg=text_color, font=font)
btn_editar.pack(fill=tk.BOTH, padx=10, pady=5)

btn_editar = tk.Button(main_frame, text="Editar", command=abrir_editar_productos, bg=button_color, fg=text_color, font=font)
btn_editar.pack(fill=tk.BOTH, padx=10, pady=5)

btn_eliminar = tk.Button(main_frame, text="Eliminar", command=eliminar, bg=button_color, fg=text_color, font=font)
btn_eliminar.pack(fill=tk.BOTH, padx=10, pady=5)

btn_consultar_productos = tk.Button(main_frame, text="Consultar productos", command=consultar_productos, bg=button_color, fg=text_color, font=font)
btn_consultar_productos.pack(fill=tk.BOTH, padx=10, pady=5)

btn_consultar_productos = tk.Button(main_frame, text="Consultar productos", command=consultar_productos, bg=button_color, fg=text_color, font=font)
btn_consultar_productos.pack(fill=tk.BOTH, padx=10, pady=5)

btn_generar_reportes = tk.Button(main_frame, text="Generar Reportes de productos", command=generar_reportes, bg=button_color, fg=text_color, font=font)
btn_generar_reportes.pack(fill=tk.BOTH, padx=10, pady=5)

# Ejecutar la aplicación
root.mainloop()
