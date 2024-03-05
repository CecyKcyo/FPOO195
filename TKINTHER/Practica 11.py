from tkinter import Tk, Frame, Button, messagebox

# Métodos
def mostrarMensajes():
    # Muestra diferentes tipos de cuadros de diálogo: información, error, advertencia y una pregunta con opciones OK/Cancelar
    print(messagebox.showinfo('showinfo', 'Information'))  # Muestra un mensaje de información
    print(messagebox.showerror('showerror', 'Error'))      # Muestra un mensaje de error
    print(messagebox.showwarning('showwarning', 'Warning'))# Muestra un mensaje de advertencia
    # Pregunta al usuario si desea continuar, mostrando un cuadro de diálogo con las opciones OK y Cancelar
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Soy el título"))
    
def addbtn():
    # Cambia el texto del botón verde a "+"
    botonVerde.config(text="+")
    # Crea y configura un nuevo botón de color rosa dentro de seccion3
    botonrosa = Button(seccion3,text="Nuevo", bg="#f7089c")
    botonrosa.configure(height=3, width=5)
    botonrosa.pack()  # Empaqueta el botón rosa para mostrarlo en la interfaz
    
# Creamos una instancia de Tk, que es la ventana principal de nuestra aplicación
ventana = Tk() 
ventana.title("Ejemplo con 3 frames")  # Título de la ventana
ventana.geometry("600x400")           # Tamaño de la ventana
 
# Creación y configuración de tres secciones (frames) con diferentes colores de fondo
seccion1 = Frame(ventana, bg="Pink")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(ventana, bg="white")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg="black")
seccion3.pack(expand=True, fill='both')

# Creación de botones en diferentes secciones usando distintos métodos de posicionamiento: place, grid y pack

# Place
botonAzul = Button(seccion1, text="Azul", fg="#0733f7")
botonAzul.place(x=60, y=60, width=500, height=30)  # Posiciona el botón azul en seccion1 usando coordenadas

# Grid
botonNegro = Button(seccion2, text="Negro", fg="Black")
botonNegro.configure(height=2, width=10)
botonNegro.grid(row=0, column=1)  # Posiciona el botón negro en una cuadrícula en seccion2

botonAmarillo = Button(seccion2, text="Amarillo", fg="#fbff00", command=mostrarMensajes)
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row=2, column=1)  # Posiciona el botón amarillo en la cuadrícula y le asigna una función

# Pack
botonVerde = Button(seccion3, text="Verde", fg="#06e813", command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()  # Posiciona el botón verde en seccion3 y le asigna una función

# Inicia el bucle principal de la ventana, esperando eventos del usuario (como clics en los botones)
ventana.mainloop()
