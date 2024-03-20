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
root.title("Editar Usuario")

# Marco principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Título
titulo_label = ttk.Label(main_frame, text="Editar Usuario", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Texto e ingreso de Nombre
nombre_label = ttk.Label(main_frame, text="Nombre(s):")
nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
nombre_entry = ttk.Entry(main_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)

# Texto e ingreso de Apellidos
apellidos_label = ttk.Label(main_frame, text="Apellidos:")
apellidos_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
apellidos_entry = ttk.Entry(main_frame)
apellidos_entry.grid(row=2, column=1, padx=5, pady=5)

# Texto e ingreso de Correo
correo_label = ttk.Label(main_frame, text="Correo:")
correo_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
correo_entry = ttk.Entry(main_frame)
correo_entry.grid(row=3, column=1, padx=5, pady=5)

# Texto e ingreso de Contraseña
contraseña_label = ttk.Label(main_frame, text="Contraseña:")
contraseña_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
contraseña_entry = ttk.Entry(main_frame)
contraseña_entry.grid(row=4, column=1, padx=5, pady=5)

# Texto e ingreso de Rol
rol_label = ttk.Label(main_frame, text="Rol:")
rol_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
rol_entry = ttk.Entry(main_frame)
rol_entry.grid(row=5, column=1, padx=5, pady=5)

# Texto e ingreso de Edad
edad_label = ttk.Label(main_frame, text="Edad:")
edad_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
edad_entry = ttk.Entry(main_frame)
edad_entry.grid(row=6, column=1, padx=5, pady=5)

# Texto e ingreso de Teléfono
telefono_label = ttk.Label(main_frame, text="Telefono:")
telefono_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
telefono_entry = ttk.Entry(main_frame)
telefono_entry.grid(row=7, column=1, padx=5, pady=5)

# Texto e ingreso de Dirección
direccion_label = ttk.Label(main_frame, text="Dirección:")
direccion_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
direccion_entry = ttk.Entry(main_frame)
direccion_entry.grid(row=8, column=1, padx=5, pady=5)

# Botón "Guardar"
save_image = load_image("C:/Users/Danie/Documents/UPQ/CUATRIMESTRE 3/VS estudio/2/save.png", 20, 20) 
guardar_button = ttk.Button(main_frame, text="Guardar", image=save_image, compound=tk.LEFT, command=guardar_articulo)
guardar_button.grid(row=9, column=1, padx=5, pady=10, sticky="e")

root.mainloop()
