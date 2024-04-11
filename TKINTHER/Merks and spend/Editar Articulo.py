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

def guardar_articulo():
    # Aquí puedes agregar la lógica para guardar el artículo
    print("Artículo editado")

root = tk.Tk()
root.title("Editar Articulo")

# Marco principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Título
titulo_label = ttk.Label(main_frame, text="Editar Artículo", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Texto "Nombre" y entrada de texto
nombre_label = ttk.Label(main_frame, text="Nombre:")
nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
nombre_entry = ttk.Entry(main_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)

# Texto "Cantidad" y entrada de texto
cantidad_label = ttk.Label(main_frame, text="Cantidad:")
cantidad_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
cantidad_entry = ttk.Entry(main_frame)
cantidad_entry.grid(row=2, column=1, padx=5, pady=5)

# Texto "Precio" y entrada de texto
precio_label = ttk.Label(main_frame, text="Precio:")
precio_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
precio_entry = ttk.Entry(main_frame)
precio_entry.grid(row=3, column=1, padx=5, pady=5)

# Botón "Guardar"
save_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/save.png", 20, 20) 
guardar_button = ttk.Button(main_frame, text="Guardar", image=save_image, compound=tk.LEFT, command=guardar_articulo)
guardar_button.grid(row=4, column=1, padx=5, pady=10, sticky="e")

root.mainloop()
