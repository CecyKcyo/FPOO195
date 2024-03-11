import tkinter as tk
from tkinter import ttk
from series import Serie

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Series")
        self.root.configure(bg="#ffccff")
        self.series = []

        # Widgets
        self.lista_series = ttk.Combobox(root, state="readonly")
        self.lista_series.grid(row=0, column=0, padx=10, pady=10)

        self.btn_reproducir = tk.Button(root, text="Reproducir", command=self.reproducir, bg="#ff99ff")
        self.btn_reproducir.grid(row=1, column=0, padx=10, pady=10)

        self.btn_agregar = tk.Button(root, text="Agregar a mi lista", command=self.agregar_a_lista, bg="#ff99ff")
        self.btn_agregar.grid(row=2, column=0, padx=10, pady=10)

        self.actualizar_lista_series()

    def actualizar_lista_series(self):
        nombres_series = [serie.titulo for serie in self.series]
        self.lista_series['values'] = nombres_series

    def reproducir(self):
        indice = self.lista_series.current()
        if indice >= 0:
            serie_seleccionada = self.series[indice]
            tk.messagebox.showinfo("Reproducir", serie_seleccionada.reproducir())

    def agregar_a_lista(self):
        # Este método sería para agregar series a la lista `self.series`
        # Aquí debería ir la lógica para agregar una nueva serie,
        # posiblemente abriendo otra ventana para ingresar los datos de la nueva serie.
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
