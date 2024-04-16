from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ControladorUsuarios import Controlador

# Creación de un objeto de la clase Controlador para manejar las operaciones CRUD con los usuarios.
objControlador = Controlador()

# Función para buscar un usuario por su ID y mostrar los resultados.
def buscarUsuarioPorID():
    id_usuario = varBus.get()
    usuario = objControlador.consultaUsuarioPorID(id_usuario)
    if usuario:
        resultado_text.delete(1.0, END)
        resultado_text.insert(END, f"ID: {usuario[0]}\nNombre: {usuario[1]}\nDepartamento: {usuario[2]}\n")
    else:
        messagebox.showinfo("Resultado", "Usuario no encontrado o no existe.")

# Crear la ventana principal.
ventana = Tk()
ventana.title("Buscar Usuario")
ventana.configure(background='white')  # Fondo blanco para diseño minimalista.

# Configuración para buscar un usuario por ID.
Label(ventana, text="Buscar Usuario", fg="black", font=("Arial", 18), bg='white').pack(pady=(10,5))
varBus = StringVar()
Label(ventana, text="Id:", bg='white').pack(pady=(5,2))
entry_busqueda = Entry(ventana, textvariable=varBus)
entry_busqueda.pack(pady=(2,5))
Button(ventana, text="Buscar Usuario", command=buscarUsuarioPorID).pack(pady=(5,10))

# Área de texto para mostrar los resultados de la búsqueda.
resultado_text = Text(ventana, height=5, width=52)
resultado_text.pack(pady=(5,10))

# Ejecutar la aplicación.
ventana.mainloop()
