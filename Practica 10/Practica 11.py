from tkinter import Tk, Frame
#1 Creamos una instancia
ventana=Tk() #Uso de poo creando objetos ventana 
ventana.title("Ejemplo con 3 frames")
ventana.geometry("600x400")

#colocamos frames de la ventana
seccion1=Frame(ventana, bg="pink")
seccion1.pack(expand=True, fill='both')

seccion2=Frame(ventana, bg="yellow")
seccion2.pack(expand=True, fill='both')

seccion3=Frame(ventana, bg="black")
seccion3.pack(expand=True, fill='both')

#Ejecutamos la ventana
ventana.mainloop()