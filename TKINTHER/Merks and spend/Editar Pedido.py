import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("MERKS AND SPEN")

# Establecer estilo
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TFrame', background="#F0F0F0")  # Establecer el color de fondo del marco principal

# Función para cargar imágenes
def load_image(file_name, width, height):
    try:
        image = Image.open(file_name)
        image = image.resize((width, height), Image.LANCZOS)  # Utilizamos Image.LANCZOS para el método de redimensionamiento
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_name}'")

# Crear el marco principal
main_frame = ttk.Frame(root, style='TFrame')
main_frame.pack(padx=20, pady=20)

# Crear el título
title_label = ttk.Label(main_frame, text="MERKS AND SPEN", style='TLabel', font=('Arial', 18, 'bold'))
title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

# Crear el subtítulo
subtitle_label = ttk.Label(main_frame, text="Editar Pedido", style='TLabel', font=('Arial', 14))
subtitle_label.grid(row=1, column=0, columnspan=4, pady=(0, 20))

# Crear la tabla de 4x4
for i in range(4):  # Filas
    for j in range(4):  # Columnas
        if i == 0:
            if j == 0:
                ttk.Label(main_frame, text="Articulos", font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
            elif j == 1:
                ttk.Label(main_frame, text="Cantidad", font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
            elif j == 2:
                ttk.Label(main_frame, text="Precio unitario", font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
            elif j == 3:
                ttk.Label(main_frame, text="Precio total", font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
        elif i == 3:
            if j == 0:
                ttk.Label(main_frame, text="Precio a pagar:", font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
                ttk.Entry(main_frame, width=30).grid(row=i+2, column=1, columnspan=3, padx=5, pady=5)
                break
        else:
            ttk.Entry(main_frame).grid(row=i+2, column=j, padx=5, pady=5)

# Cargar la imagen de "plus.png"
plus_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/plus.png", 20, 20)

# Agregar el botón "Agregar"
add_button = ttk.Button(main_frame, image=plus_image)
add_button.grid(row=7, column=3, padx=(0, 20), pady=10, sticky="e")

# Texto "Agregar" afuera del botón
add_label = ttk.Label(main_frame, text="Agregar", font=('Arial', 12))
add_label.grid(row=7, column=2, pady=10, sticky="e")

# Ejecutar la ventana
root.mainloop()
