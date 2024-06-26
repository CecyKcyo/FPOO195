from tkinter import messagebox
import sqlite3 
import bcrypt


class Controlador:
    # Método para establecer conexión con la base de datos SQLite
    def conexion(self):
        try:
            # Intenta conectar a la base de datos especificada por la ruta
            conex = sqlite3.connect("D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/bdMerks.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            # Captura el error si no puede conectar a la base de datos
            print("No se pudo conectar, que tibio")

    # Método para encriptar la contraseña del usuario
    def encriptapass(self, cont):
        # Convierte la contraseña en texto plano a bytes
        passPlana = cont.encode()
        # Genera una 'sal' aleatoria para el proceso de encriptación
        sal = bcrypt.gensalt()
        # Encripta la contraseña utilizando bcrypt
        passHash = bcrypt.hashpw(passPlana, sal)
        return passHash

    # Método para insertar un nuevo usuario en la base de datos
    def insertUsuario(self, nom, contra, dep):
        # Establece la conexión con la base de datos
        conexion = self.conexion()
        # Verifica si alguno de los campos está vacío
        if (nom == "" or contra == "" or dep == ""):
            # Muestra una advertencia si algún campo está vacío
            messagebox.showwarning("Cuidado", "No seas tibio, llena todos los campos")
            conexion.close()
        else:
            # Crea un cursor para realizar operaciones en la base de datos
            cursor = conexion.cursor()
            # Encripta la contraseña antes de insertarla
            contraH = self.encriptapass(contra)
            # Prepara los datos para la inserción
            datos = (nom, contraH, dep)
            # Sentencia SQL para insertar el nuevo usuario
            sqlinsert = "INSERT INTO usuarios(nombre, contrasena, departamento) VALUES (?, ?, ?)"
            
            # Ejecuta la sentencia SQL con los datos proporcionados
            cursor.execute(sqlinsert, datos)
            # Confirma los cambios en la base de datos
            conexion.commit()
            # Cierra la conexión con la base de datos
            conexion.close()
            # Muestra una notificación de éxito
            messagebox.showinfo("Éxito", "Registro exitoso! ESOOOO TILIN")
            
            
    def consultaUsuarioPorID(self, id):
        conexion = self.conexion()
        cursor = conexion.cursor()
        # Preparar la sentencia SQL para seleccionar el usuario por ID
        sqlconsulta = "SELECT id, nombre, departamento FROM usuarios WHERE id = ?"
        cursor.execute(sqlconsulta, (id,))
        # Obtener el primer resultado, el fetchone retorna un registro 
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
           
            print("Ese vato si existe :", usuario)
            return usuario
        else:
            messagebox.showwarning("Error", "Ese usuario no existe tibio.")
            return None
        
    # Método para consultar todos los usuarios 
    def consultarUsuarios(self):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, contrasena, departamento FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al consultar usuarios: {e}")
        finally:
            if conexion:
                conexion.close()
    
  
    def actualizarUsuario(self, id, nom, contra, depa):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            # Encripta la nueva contraseña antes de actualizar
            contraH = self.encriptapass(contra)
            datos = (nom, contraH, depa, id)
            sqlupdate = "UPDATE usuarios SET nombre = ?, contrasena = ?, departamento = ? WHERE id = ?"
            cursor.execute(sqlupdate, datos)
            conexion.commit()
        except Exception as e:
            messagebox.showerror("Error al actualizar", f"Error: {e}")
        finally:
            conexion.close()
            messagebox.showinfo("Actualización", "Usuario actualizado con éxito")
    
    def eliminarUsuario(self, id):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            sqldelete = "DELETE FROM usuarios WHERE id = ?"
            cursor.execute(sqldelete, (id,))
            conexion.commit()
        except Exception as e:
            messagebox.showerror("Error al eliminar", f"Error: {e}")
        finally:
            conexion.close()
            messagebox.showinfo("Eliminación", "Usuario eliminado con éxito")




 