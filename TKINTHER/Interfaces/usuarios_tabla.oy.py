import tkinter as tk
from tkinter import ttk

# Función para simular la acción de los botones
def accion_boton():
    print("Botón presionado")

# Inicializa la ventana principal
ventana = tk.Tk()
ventana.title("MERKS AND SPEN - Administrador de usuarios")

# Frame para el título
frame_titulo = tk.Frame(ventana)
frame_titulo.pack(fill=tk.X)

# Etiqueta del título
titulo = tk.Label(frame_titulo, text="MERKS AND SPEN\nAdministrador de usuarios", font=("Arial", 16))
titulo.pack(side=tk.LEFT)

# Botón para agregar usuario
boton_agregar = tk.Button(frame_titulo, text="Agregar", command=accion_boton)
boton_agregar.pack(side=tk.LEFT)

# Campo de búsqueda de usuario
busqueda_usuario = tk.Entry(frame_titulo)
busqueda_usuario.pack(side=tk.RIGHT)
boton_buscar = tk.Button(frame_titulo, text="Buscar", command=accion_boton)
boton_buscar.pack(side=tk.RIGHT)

# Tabla para mostrar los usuarios
tabla = ttk.Treeview(ventana, columns=("id", "nombre", "apellidos", "rol", "correo", "contrasena"), show="headings")
tabla.pack(expand=True, fill=tk.BOTH)

# Definiendo los encabezados de la tabla
tabla.heading("id", text="Id")
tabla.heading("nombre", text="Nombre")
tabla.heading("apellidos", text="Apellidos")
tabla.heading("rol", text="Rol")
tabla.heading("correo", text="Correo")
tabla.heading("contrasena", text="Contraseña")


# Agregando las columnas de botones
for i in range(10):  # Suponiendo que tienes 10 usuarios
    tabla.insert('', 'end', values=(i, "Nombre"+str(i), "Apellido"+str(i), "Rol"+str(i), "Correo"+str(i), "*****"))
    boton_editar = tk.Button(ventana, text="Editar", command=accion_boton)
    boton_editar.pack()
    boton_eliminar = tk.Button(ventana, text="Eliminar", command=accion_boton)
    boton_eliminar.pack()
    boton_guardar = tk.Button(ventana, text="Guardar", command=accion_boton)
    boton_guardar.pack()

# Iniciar el bucle principal
ventana.mainloop()
