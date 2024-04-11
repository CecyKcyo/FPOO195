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
title_label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

# Crear el subtítulo
subtitle_label = ttk.Label(main_frame, text="Reporte de Venta", style='TLabel', font=('Arial', 14))
subtitle_label.grid(row=1, column=0, columnspan=5, pady=(0, 20))

# Crear la tabla de 8x5
for i in range(5):  # Filas
    for j in range(5):  # Columnas
        if i == 0:
            ttk.Label(main_frame, text=["Id", "Articulos", "Cantidad", "Tipo de pago", "Precio Total"][j],
                      font=('Arial', 12, 'bold')).grid(row=i+2, column=j, padx=5, pady=5)
        else:
            ttk.Entry(main_frame).grid(row=i+2, column=j, padx=5, pady=5)


save_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/save.png", 20, 20)

# Agregar botón Generar Reporte con la imagen de save.png
#generate_report_button = ttk.Button(main_frame, text="Descargar", image=save_image, compound=tk.LEFT)
#generate_report_button.grid(row=7, column=0, columnspan=5, pady=10, padx=(0, 20), sticky="e")

# Ejecutar la ventana
root.mainloop()
