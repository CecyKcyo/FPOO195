import tkinter as tk

# Función para crear la interfaz de inicio de sesión
def create_login_interface():
    # Crear una nueva ventana de Tkinter
    window = tk.Tk()

    # Establecer el título de la ventana
    window.title("MERKS AND SPEN")

    # Establecer el tamaño de la ventana
    window.geometry("400x200")

    # Crear un frame para el logo
    logo_frame = tk.Frame(window)
    logo_frame.pack(side=tk.TOP, pady=10)

    # Añadir una etiqueta para el logo
    logo_label = tk.Label(logo_frame, text="MERKS AND SPEN", font=("Arial", 16))
    logo_label.pack()

    # Crear un frame para el formulario
    form_frame = tk.Frame(window)
    form_frame.pack(side=tk.TOP, pady=10)

    # Añadir una etiqueta y entrada para el correo
    email_label = tk.Label(form_frame, text="Correo:", font=("Arial", 12))
    email_label.grid(row=0, column=0, sticky=tk.W, pady=2)
    email_entry = tk.Entry(form_frame, width=30)
    email_entry.grid(row=0, column=1, pady=2)

    # Añadir una etiqueta y entrada para la contraseña
    password_label = tk.Label(form_frame, text="Contraseña:", font=("Arial", 12))
    password_label.grid(row=1, column=0, sticky=tk.W, pady=2)
    password_entry = tk.Entry(form_frame, width=30, show="*")
    password_entry.grid(row=1, column=1, pady=2)

    # Añadir un botón de inicio de sesión
    login_button = tk.Button(window, text="INICIAR SESIÓN", bg="grey", font=("Arial", 12))
    login_button.pack(side=tk.TOP, pady=10)

    # Ejecutar el bucle de eventos de Tkinter
    window.mainloop()

# Llamar a la función para crear la interfaz de inicio de sesión
create_login_interface()