from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Controlador import Controlador

# Creación de un objeto de la clase Controlador para manejar las operaciones CRUD.
objControlador = Controlador()

# Función que se llamará al presionar el botón de guardar usuario.
def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

def buscarUsuarioPorID():
    id_usuario = varBus.get()
    usuario = objControlador.consultaUsuarioPorID(id_usuario)
    if usuario:
        resultado_text.delete(1.0, END)
        resultado_text.insert(END, f"ID: {usuario[0]}\nNombre: {usuario[1]}\nCorreo: {usuario[2]}\n")
    else:
        messagebox.showinfo("Resultado", "Usuario no encontrado o no existe.")

def cargarUsuarios():
    
    for i in listaUsuarios.get_children():
        listaUsuarios.delete(i)
   
    for usuario in objControlador.consultarUsuarios():
        listaUsuarios.insert("", "end", values=usuario)
        


# Configuración inicial de la ventana
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")

# Configuración de la pestaña 1: Crear usuario
Label(pestana1, text="Registro de Usuarios", fg="Pink", font=("Modern", 18)).pack()
var1 = tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()
var2 = tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()
var3 = tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3, show='*').pack()
Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

# Configuración de la pestaña 2: Buscar Usuario
Label(pestana2, text="Buscar Usuario", fg="Pink", font=("Modern", 18)).pack()
varBus = tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()
Button(pestana2, text="Buscar Usuario", command=buscarUsuarioPorID).pack()
resultado_text = tk.Text(pestana2, height=5, width=52)
resultado_text.pack()

# Configuración de la pestaña 3: Consultar Usuarios
Label(pestana3, text="Lista de Usuarios", fg="Pink", font=("Modern", 18)).pack()
cols = ('ID', 'Nombre', 'Correo', 'Contraseña')
listaUsuarios = ttk.Treeview(pestana3, columns=cols, show='headings')
for col in cols:
    listaUsuarios.heading(col, text=col)
listaUsuarios.pack(fill='both', expand=True)
Button(pestana3, text="Cargar Usuarios", command=cargarUsuarios).pack()


ventana.mainloop()
