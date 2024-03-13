import tkinter as tk
from tkinter import ttk

# Configuración inicial de la ventana
ventana = tk.Tk()
ventana.title("MERKS AND SPEN - Administrador de usuarios")

# Estilo del Treeview
estilo = ttk.Style()
estilo.theme_use("clam")  # El tema 'clam' permite cambiar el color de fondo

# Definir el color de fondo del encabezado y las filas
estilo.configure("Treeview.Heading", background="#003366", foreground="white", font=('Calibri', 10, 'bold'))
estilo.configure("Treeview", background="white", foreground="black", rowheight=25, font=('Calibri', 10))

# Agregar tabla Treeview
tabla = ttk.Treeview(ventana, columns=("Id", "Nombre", "Apellidos", "Rol", "Correo", "Contraseña", "Editar", "Eliminar", "Guardar"), show="headings")
tabla.pack(expand=True, fill="both")

# Configuración de las columnas
tabla.column("Id", width=20, anchor="center")
tabla.column("Nombre", width=120, anchor="center")
tabla.column("Apellidos", width=120, anchor="center")
tabla.column("Rol", width=80, anchor="center")
tabla.column("Correo", width=150, anchor="center")
tabla.column("Contraseña", width=80, anchor="center")
tabla.column("Editar", width=50, anchor="center")
tabla.column("Eliminar", width=50, anchor="center")
tabla.column("Guardar", width=50, anchor="center")

# Configuración de los encabezados
tabla.heading("Id", text="Id")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Apellidos", text="Apellidos")
tabla.heading("Rol", text="Rol")
tabla.heading("Correo", text="Correo")
tabla.heading("Contraseña", text="Contraseña")
tabla.heading("Editar", text="Editar")
tabla.heading("Eliminar", text="Eliminar")
tabla.heading("Guardar", text="Guardar")

# Botón Agregar y barra de búsqueda (placeholder)
frame_superior = tk.Frame(ventana)
frame_superior.pack(fill="x", pady=10)

boton_agregar = tk.Button(frame_superior, text="Agregar", padx=10, pady=2)
boton_agregar.pack(side="left", padx=10)

entrada_buscar = tk.Entry(frame_superior)
entrada_buscar.pack(side="right", padx=10)

boton_buscar = tk.Button(frame_superior, text="Buscar", padx=10, pady=2)
boton_buscar.pack(side="right")

# Agregar datos de prueba a la tabla
for i in range(1, 6):
    boton_editar = tk.Button(ventana, text="Editar")
    boton_eliminar = tk.Button(ventana, text="Eliminar")
    boton_guardar = tk.Button(ventana, text="Guardar")
    
    tabla.insert('', 'end', values=(
        i,
        "Nombre{}".format(i),
        "Apellido{}".format(i),
        "Rol{}".format(i),
        "correo{}@ejemplo.com".format(i),
        "*****",
        boton_editar,
        boton_eliminar,
        boton_guardar
    ))

# Función para actualizar los botones dentro de la tabla
def actualizar_botones():
    for i in tabla.get_children():
        tabla.set(i, column="Editar", value="Editar")
        tabla.set(i, column="Eliminar", value="Eliminar")
        tabla.set(i, column="Guardar", value="Guardar")

# Llamar a la función actualizar_botones después de que la ventana esté completamente cargada
ventana.after(100, actualizar_botones)

ventana.mainloop()
