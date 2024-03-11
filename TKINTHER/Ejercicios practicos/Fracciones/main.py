# main.py

import tkinter as tk
from fracciones import Fraccion

def calcular():
    try:
        fraccion1 = Fraccion(int(entrada_numerador1.get()), int(entrada_denominador1.get()))
        fraccion2 = Fraccion(int(entrada_numerador2.get()), int(entrada_denominador2.get()))

        if operacion.get() == '+':
            resultado = fraccion1 + fraccion2
        elif operacion.get() == '-':
            resultado = fraccion1 - fraccion2
        elif operacion.get() == '*':
            resultado = fraccion1 * fraccion2
        elif operacion.get() == '/':
            resultado = fraccion1 / fraccion2
        else:
            resultado = "Operación no soportada"

        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except Exception as e:
        etiqueta_resultado.config(text=f"Error: {str(e)}")

ventana = tk.Tk()
ventana.title("Operaciones con Fracciones")
ventana.config(bg="#FFC0CB")

etiqueta_numerador1 = tk.Label(ventana, text="Numerador 1:", bg="#FFC0CB")
etiqueta_numerador1.grid(row=0, column=0)
entrada_numerador1 = tk.Entry(ventana)
entrada_numerador1.grid(row=0, column=1)

etiqueta_denominador1 = tk.Label(ventana, text="Denominador 1:", bg="#FFC0CB")
etiqueta_denominador1.grid(row=1, column=0)
entrada_denominador1 = tk.Entry(ventana)
entrada_denominador1.grid(row=1, column=1)

etiqueta_numerador2 = tk.Label(ventana, text="Numerador 2:", bg="#FFC0CB")
etiqueta_numerador2.grid(row=2, column=0)
entrada_numerador2 = tk.Entry(ventana)
entrada_numerador2.grid(row=2, column=1)

etiqueta_denominador2 = tk.Label(ventana, text="Denominador 2:", bg="#FFC0CB")
etiqueta_denominador2.grid(row=3, column=0)
entrada_denominador2 = tk.Entry(ventana)
entrada_denominador2.grid(row=3, column=1)

operacion = tk.StringVar()
operacion.set('+')
opciones_operacion = tk.OptionMenu(ventana, operacion, '+', '-', '*', '/')
opciones_operacion.config(bg="#FFC0CB")
opciones_operacion.grid(row=4, column=0, columnspan=2)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular, bg="#FFB6C1")
boton_calcular.grid(row=5, column=0, columnspan=2)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ", bg="#FFC0CB")
etiqueta_resultado.grid(row=6, column=0, columnspan=2)

ventana.mainloop()
