from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from GenerarReporteUsu import GeneradorPDF
from ConsultarUsuarios import Controlador  # Asegúrate de importar correctamente la clase
import os

# Inicializa los objetos del controlador y del generador de PDF.
objControl2 = Controlador()
objPDF = GeneradorPDF()

def ejecutaPdf():
    titulo = varTitulo.get()
    if titulo.strip() == "":
        messagebox.showwarning("Importante", "Escribe un nombre al PDF")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(titulo + ".pdf")
        rutaPDF = f"D:/Fundamentos de programacion/FPOO195/TKINTHER/TKSQLITE/{titulo}.pdf"
        messagebox.showinfo("Archivo creado", f"PDF disponible en carpeta: {rutaPDF}")
        os.system(f"start {rutaPDF}")

# Configura la ventana principal
ventana = tk.Tk()
ventana.title("Generador de PDF")
ventana.geometry("400x200")  # Ajusta el tamaño según necesites

# Etiqueta de título
Label(ventana, text="Reporte de usuarios PDF", fg="Green", font=("Mono", 18)).pack(pady=10)

# Entrada para el título del PDF
varTitulo = tk.StringVar()
Label(ventana, text="Escribe el título del PDF:").pack()
entry_titulo = Entry(ventana, textvariable=varTitulo)
entry_titulo.pack()

# Botón para crear el PDF
Button(ventana, text="Crear PDF", command=ejecutaPdf).pack(pady=10)

ventana.mainloop()
