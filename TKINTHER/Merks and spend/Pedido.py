import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def load_image(file_name, width, height):
    try:
        image = Image.open(file_name)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_name}'")

root = tk.Tk()
root.title("MERKS AND SPEN")

style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TFrame', background="#F0F0F0")

main_frame = ttk.Frame(root, style='TFrame')
main_frame.pack(padx=20, pady=20)

title_label = ttk.Label(main_frame, text="MERKS AND SPEN", style='TLabel', font=('Arial', 18, 'bold'))
title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

subtitle_label = ttk.Label(main_frame, text="Editar Pedido", style='TLabel', font=('Arial', 14))
subtitle_label.grid(row=1, column=0, columnspan=4, pady=(0, 20))

# Crear la tabla de 4x4
headers = ["Artículos", "Cantidad", "Precio unitario", "Precio total"]
for j, header in enumerate(headers):
    ttk.Label(main_frame, text=header, font=('Arial', 12, 'bold')).grid(row=2, column=j, padx=5, pady=5)

for i in range(3):
    for j in range(4):
        entry = ttk.Entry(main_frame)
        entry.grid(row=i+3, column=j, padx=5, pady=5)
        entry.config(font=('Arial', 12))  # Ajustar el estilo de la entrada

# Precio a pagar
ttk.Label(main_frame, text="Precio a pagar:", font=('Arial', 12, 'bold')).grid(row=6, column=0, padx=5, pady=5)
precio_entry = ttk.Entry(main_frame, width=30)
precio_entry.grid(row=6, column=1, columnspan=3, padx=5, pady=5)
precio_entry.config(font=('Arial', 12))  # Ajustar el estilo del campo de precio

# Tipo de pago
tipo_pago_label = ttk.Label(main_frame, text="Tipo de pago:", font=('Arial', 12, 'bold'))
tipo_pago_label.grid(row=8, column=0, padx=5, pady=5)

# Cargar imágenes y mostrarlas en etiquetas
billetes_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/Billetes.png", 40, 40)
billetes_label = ttk.Label(main_frame, image=billetes_image)
billetes_label.grid(row=8, column=1, padx=5, pady=5)

tarjetas_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/Tarjeta.png", 40, 40)
tarjetas_label = ttk.Label(main_frame, image=tarjetas_image)
tarjetas_label.grid(row=8, column=2, padx=5, pady=5)

# Botón Agregar
plus_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/plus.png", 40, 40)
add_button = ttk.Button(main_frame, image=plus_image)
add_button.grid(row=7, column=3, padx=(0, 20), pady=10, sticky="e")

add_label = ttk.Label(main_frame, text="Agregar", font=('Arial', 12))
add_label.grid(row=7, column=2, pady=10, sticky="e")

root.mainloop()
