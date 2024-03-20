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
title_label.grid(row=0, column=0, columnspan=8, pady=(0, 10))

# Crear el subtítulo
subtitle_label = ttk.Label(main_frame, text="Administrador de Artículos", style='TLabel', font=('Arial', 14))
subtitle_label.grid(row=1, column=0, columnspan=8, pady=(0, 20))

# Crear la tabla de 8x5
for i in range(5):  # Filas
    for j in range(8):  # Columnas
        if i == 0:
            ttk.Label(main_frame, text=["Id", "Articulo", "Cantidad", "Fecha de entrada", "Precio", "Editar", "Eliminar", "Guardar"][j],
                      font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
        else:
            ttk.Entry(main_frame).grid(row=i+2, column=j, padx=5, pady=5)

# Cargar imágenes
edit_image = load_image("C:/Users/Danie/Documents/UPQ/CUATRIMESTRE 3/VS estudio/2/edit.png", 20, 20)
delete_image = load_image("C:/Users/Danie/Documents/UPQ/CUATRIMESTRE 3/VS estudio/2/delete.png", 20, 20)
save_image = load_image("C:/Users/Danie/Documents/UPQ/CUATRIMESTRE 3/VS estudio/2/save.png", 20, 20)

# Mostrar imágenes en cada celda correspondiente
for i, image in enumerate([edit_image, delete_image, save_image]):
    for j in range(5, 8):  # Columnas correspondientes a las imágenes
        for row in range(3, 7):  # Filas correspondientes a las imágenes
            canvas = tk.Canvas(main_frame, width=20, height=20)
            canvas.create_image(10, 10, anchor=tk.CENTER, image=image)
            canvas.grid(row=row, column=j, padx=5, pady=5)
# Ejecutar la ventana
root.mainloop()
