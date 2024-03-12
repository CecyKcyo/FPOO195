# Crea un programa con interface  en tkinter y su clase en archivos propios que solicite Nombre, Apellido_Paterno, Apellido_Materno, Año de nacimiento y carrera 
# Con los datos solicitados la interface debe genrarar una matricula con las siguientes caracteristicas:
# -3 primeras letras de la carrera 
# -2 digitos del año de nacimiento
# -primera letra del nombre 
# -3 letras del apellido paterno 
# -3 letras del apellido materno
# -3 digitos aleatorios 



import tkinter as tk
from generador_matricula import generar_matricula
from tkinter import messagebox

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Generador de Matrícula")

        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.grid(row=0, column=1)

        self.label_apellido_paterno = tk.Label(master, text="Apellido Paterno:")
        self.label_apellido_paterno.grid(row=1, column=0)
        self.entry_apellido_paterno = tk.Entry(master)
        self.entry_apellido_paterno.grid(row=1, column=1)

        self.label_apellido_materno = tk.Label(master, text="Apellido Materno:")
        self.label_apellido_materno.grid(row=2, column=0)
        self.entry_apellido_materno = tk.Entry(master)
        self.entry_apellido_materno.grid(row=2, column=1)

        self.label_año_curso = tk.Label(master, text="Año en curso:")
        self.label_año_curso.grid(row=3, column=0)
        self.entry_año_curso = tk.Entry(master)
        self.entry_año_curso.grid(row=3, column=1) 
        
        self.label_año_nacimiento = tk.Label(master, text="Año de Nacimiento:")
        self.label_año_nacimiento.grid(row=4, column=0)
        self.entry_año_nacimiento = tk.Entry(master)
        self.entry_año_nacimiento.grid(row=4, column=1)

        self.label_carrera = tk.Label(master, text="Carrera:")
        self.label_carrera.grid(row=5, column=0)
        self.entry_carrera = tk.Entry(master)
        self.entry_carrera.grid(row=5, column=1)

        self.button_generar_matricula = tk.Button(master, text="Generar Matrícula", command=self.generar_matricula)
        self.button_generar_matricula.grid(row=6, columnspan=2)

        self.label_matricula = tk.Label(master, text="")
        self.label_matricula.grid(row=7, columnspan=2)

    def generar_matricula(self):
        nombre = self.entry_nombre.get().strip()
        apellido_paterno = self.entry_apellido_paterno.get().strip()
        apellido_materno = self.entry_apellido_materno.get().strip()
        año_curso = self.entry_año_curso.get().strip()
        año_nacimiento = self.entry_año_nacimiento.get().strip()
        carrera = self.entry_carrera.get().strip()

        if nombre and apellido_paterno and apellido_materno and año_curso and año_nacimiento and carrera:
            matricula = generar_matricula(nombre, apellido_paterno, apellido_materno,año_curso, año_nacimiento, carrera)
            messagebox.showinfo("Tu matricula es", f"Tu matricula es: {matricula}")
        else:
            self.label_matricula.config(text="Te faltan datos tibio")

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
