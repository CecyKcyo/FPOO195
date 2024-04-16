from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox 
from ControladorAgregarProducto import Controlador  # Asume que tienes un controlador similar para productos
from PIL import Image, ImageTk

objControlador = Controlador()

def confirmar_y_eliminar():
    # Recuperamos el ID del producto de la entrada
    id_producto = id_entry.get()
    # Mostramos un cuadro de diálogo para confirmar la eliminación
    if messagebox.askyesno("Confirmar Eliminación", f"Estás a punto de eliminar el producto con ID: {id_producto}\n¿Deseas proceder?"):
        ejecutaEliminar()

def ejecutaEliminar():
    try:
        if objControlador.eliminarProducto(id_entry.get()):
            messagebox.showinfo("Eliminación Exitosa", "El producto ha sido eliminado exitosamente.")
            root.destroy()  # Cierra la ventana si la eliminación fue exitosa
        else:
            messagebox.showwarning("Eliminación Fallida", "El producto no se pudo eliminar.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al eliminar el producto: {e}")

def load_image(file_name, width, height):
    try:
        image = Image.open(file_name)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_name}'")

root = tk.Tk()
root.title("Eliminar Producto")

# Marco principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Título
titulo_label = ttk.Label(main_frame, text="Eliminar Producto", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campo para ingresar el ID del producto a eliminar
id_label = ttk.Label(main_frame, text="Ingresa el ID del producto a eliminar:")
id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
id_entry = ttk.Entry(main_frame)
id_entry.grid(row=1, column=1, padx=5, pady=5)

# Botón "Eliminar"
delete_image = load_image("C:/Users/maner/OneDrive/Escritorio/POO/Merks-and-Spen/save.png", 20, 20) 
eliminar_button = ttk.Button(main_frame, text="Eliminar", image=delete_image, compound=tk.LEFT, command=confirmar_y_eliminar)
eliminar_button.grid(row=2, column=1, padx=5, pady=10, sticky="e")

root.mainloop()
