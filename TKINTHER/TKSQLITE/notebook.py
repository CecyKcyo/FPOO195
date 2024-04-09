from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Controlador import Controlador
from  GeneradorPDF import *
import os 


# Creación de un objeto de la clase Controlador para manejar las operaciones CRUD.
objControlador = Controlador()
objPDF=GeneradorPDF()

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
def ejecutaPdf():
    if varTitulo==" ":
        messagebox.showwarning("Importante", "Escribe un nombre al PDF")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(str(varTitulo.get())+".pdf")
        rutaPDF= "D:/Fundamentos de programacion/FPOO195/TKINTHER/TKSQLITE/"+varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado", "PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")
        
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
pestana6 = ttk.Frame(panel)


panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")
panel.add(pestana6, text="Reporte PDF")

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

# Pestaña de Edición de Usuario
Label(pestana4, text="Editar Usuario", fg="Pink", font=("Modern", 18)).pack()

varEditId = tk.StringVar()
Label(pestana4, text="ID: ").pack()
Entry(pestana4, textvariable=varEditId).pack()

varEditNombre = tk.StringVar()
Label(pestana4, text="Nuevo Nombre: ").pack()
Entry(pestana4, textvariable=varEditNombre).pack()

varEditCorreo = tk.StringVar()
Label(pestana4, text="Nuevo Correo: ").pack()
Entry(pestana4, textvariable=varEditCorreo).pack()

varEditContra = tk.StringVar()
Label(pestana4, text="Nueva Contraseña: ").pack()
Entry(pestana4, textvariable=varEditContra, show='*').pack()

def ejecutaActualizar():
    objControlador.actualizarUsuario(varEditId.get(), varEditNombre.get(), varEditCorreo.get(), varEditContra.get())
    cargarUsuarios()  # Actualiza la lista de usuarios en la pestaña de consulta

Button(pestana4, text="Actualizar Usuario", command=ejecutaActualizar).pack()


# Pestaña de Eliminación de Usuario
Label(pestana5, text="Eliminar Usuario", fg="Pink", font=("Modern", 18)).pack()

varDeleteId = tk.StringVar()
Label(pestana5, text="ID del Usuario a Eliminar: ").pack()
Entry(pestana5, textvariable=varDeleteId).pack()

def ejecutaEliminar():
    objControlador.eliminarUsuario(varDeleteId.get())
    cargarUsuarios()  # Actualiza la lista de usuarios en la pestaña de consulta

Button(pestana5, text="Eliminar Usuario", command=ejecutaEliminar).pack()

# Configuración de la pestaña 6: Generador PDF
Label(pestana6, text="Reporte usuarios PDF", fg="Green", font=("Mono", 18)).pack()
varTitulo=tk.StringVar()
Label(pestana6, text="Escribe el titulo del pdf:").pack()
Entry(pestana6, textvariable=varTitulo).pack()
Button(pestana6, text="Crear PDF", command=ejecutaPdf).pack()

ventana.mainloop()
