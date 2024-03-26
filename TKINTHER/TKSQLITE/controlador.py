from tkinter import messagebox
import sqlite3 
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex = sqlite3.connect("D:/Fundamentos de programacion/FPOO195/TKINTHER/TKSQLITE/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")

    def encriptapass(self, cont):
        passPlana = cont.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana, sal)
        return passHash

    def insertUsuario(self, nom, corr, cont):
        conexion = self.conexion()
        if (nom == "" or corr == "" or cont == ""):
            messagebox.showwarning("Cuidado", "Inputs vacíos")
            conexion.close()
        else:
            cursor = conexion.cursor()
            conH = self.encriptapass(cont)
            datos = (nom, corr, conH)
            sqlinsert = "INSERT INTO tbUsuarios(nombre, correo, contra) VALUES (?, ?, ?)"
            
            cursor.execute(sqlinsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Registro exitoso!")