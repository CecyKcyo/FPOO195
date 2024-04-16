from tkinter import *
from tkinter import ttk
from ControladorUsuarios import Controlador

# Creación de un objeto de la clase Controlador para manejar las operaciones CRUD con los usuarios.
objControlador = Controlador()

# Función para cargar los usuarios en la vista de árbol (Treeview).
def cargarUsuarios():
    # Limpiar los elementos previos de la vista de árbol.
    for i in listaUsuarios.get_children():
        listaUsuarios.delete(i)
    # Añadir nuevos datos a la vista de árbol.
    for usuario in objControlador.consultarUsuarios():
        listaUsuarios.insert("", "end", values=usuario)

# Crear la ventana principal.
ventana = Tk()
ventana.title("Usuarios")
# Configurar el color de fondo de la ventana como blanco para un diseño minimalista.
ventana.configure(background='white')

# Agregar un título a la ventana con un diseño minimalista.
titulo_label = Label(ventana, text="Lista de Usuarios", bg='white', font=("Arial", 14))
titulo_label.pack(pady=(10, 0))  # Margen vertical para el título.

# Definir las columnas para la Treeview, que es la vista de árbol donde se mostrarán los datos de los usuarios.
cols = ('ID', 'Nombre', 'Correo', 'Contraseña')
listaUsuarios = ttk.Treeview(ventana, columns=cols, show='headings', height=8)

# Definir los encabezados y empaquetar la Treeview en la ventana.
for col in cols:
    listaUsuarios.heading(col, text=col)  # Establecer el texto del encabezado con el nombre de la columna.
listaUsuarios.pack(fill='both', expand=True)  # Permitir que la Treeview se expanda con la ventana.

# Agregar un botón para cargar los usuarios en la Treeview.
boton_cargar = Button(ventana, text="Cargar Usuarios", command=cargarUsuarios, bg='white', fg='black')
boton_cargar.pack(pady=(10, 10))  # Margen vertical para el botón.

# Ejecutar la aplicación.
ventana.mainloop()
