import tkinter as tk
from tkinter import simpledialog
import subprocess

# Funciones para los botones
def abrir_editar_usuarios():
    # Aquí ejecutamos el archivo Python en una nueva ventana
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Editar Usuarios.py'])
def agregar_usuario():
    # Aquí ejecutamos el archivo Python en una nueva ventana
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Agregar Usuarios.py'])

def eliminar():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Eliminar Usuario.py'])
def consultar_usuario():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Consultar Usuario.py'])
def consultar_usuarios():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/Consultar Usuarios.py'])

def generar_reportes():
    subprocess.run(['python', 'D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/ReporteUsuarios.py'])

# Crear la ventana principal
root = tk.Tk()
root.title("USUARIOS")

# Diseño minimalista: colores y fuente
background_color = "#ffffff"
button_color = "#f0f0f0"
text_color = "#333333"
font = ("Arial", 12)

# Aplicar colores de fondo y de fuente
root.configure(bg=background_color)

# Crear el título "USUARIOS"
lbl_titulo = tk.Label(root, text="USUARIOS", font=("Arial", 18), bg=background_color, fg=text_color)
lbl_titulo.pack(pady=10)

# Crear el marco principal
main_frame = tk.Frame(root, bg=background_color)
main_frame.pack(padx=20, pady=20)

# Crear los botones con un diseño minimalista
btn_editar = tk.Button(main_frame, text="Agregar", command=agregar_usuario, bg=button_color, fg=text_color, font=font)
btn_editar.pack(fill=tk.BOTH, padx=10, pady=5)

btn_editar = tk.Button(main_frame, text="Editar", command=abrir_editar_usuarios, bg=button_color, fg=text_color, font=font)
btn_editar.pack(fill=tk.BOTH, padx=10, pady=5)

btn_eliminar = tk.Button(main_frame, text="Eliminar", command=eliminar, bg=button_color, fg=text_color, font=font)
btn_eliminar.pack(fill=tk.BOTH, padx=10, pady=5)

btn_consultar_usuario = tk.Button(main_frame, text="Consultar Usuario", command=consultar_usuario, bg=button_color, fg=text_color, font=font)
btn_consultar_usuario.pack(fill=tk.BOTH, padx=10, pady=5)

btn_consultar_usuarios = tk.Button(main_frame, text="Consultar USUARIOS", command=consultar_usuarios, bg=button_color, fg=text_color, font=font)
btn_consultar_usuarios.pack(fill=tk.BOTH, padx=10, pady=5)

btn_generar_reportes = tk.Button(main_frame, text="Generar Reportes de Usuarios", command=generar_reportes, bg=button_color, fg=text_color, font=font)
btn_generar_reportes.pack(fill=tk.BOTH, padx=10, pady=5)

# Ejecutar la aplicación
root.mainloop()
