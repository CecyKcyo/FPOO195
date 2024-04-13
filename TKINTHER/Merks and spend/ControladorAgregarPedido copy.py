from tkinter import messagebox
import sqlite3 



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

  
    # Método para insertar un nuevo pedido en la base de datos
    def insertPedido(self, departamento, producto, cantidad, fecha, status):
        # Establece la conexión con la base de datos
        conexion = self.conexion()
        # Verifica si alguno de los campos está vacío
        if (departamento == "" or producto == "" or cantidad == "" or fecha == "" or status == ""):
            # Muestra una advertencia si algún campo está vacío
            messagebox.showwarning("Cuidado", "No seas tibio, llena todos los campos")
            conexion.close()
        else:
            # Crea un cursor para realizar operaciones en la base de datos
            cursor = conexion.cursor()
            
            # Prepara los datos para la inserción
            datos = (departamento, producto, cantidad, fecha, status)
            # Sentencia SQL para insertar el nuevo pedido
            sqlinsert = "INSERT INTO pedidos(departamento, producto, cantidad, fecha, status) VALUES (?, ?, ?,?,')"
            
            # Ejecuta la sentencia SQL con los datos proporcionados
            cursor.execute(sqlinsert, datos)
            # Confirma los cambios en la base de datos
            conexion.commit()
            # Cierra la conexión con la base de datos
            conexion.close()
            # Muestra una notificación de éxito
            messagebox.showinfo("Éxito", "Registro exitoso! ESOOOO TILIN")
            
            
    def consultaPedidoPorId(self, id):
        conexion = self.conexion()
        cursor = conexion.cursor()
        # Preparar la sentencia SQL para seleccionar el pedido por ID
        sqlconsulta = "SELECT id, departamento, producto, cantidad, fecha, status FROM pedidos WHERE id = ?"
        cursor.execute(sqlconsulta, (id,))
        # Obtener el primer resultado, el fetchone retorna un registro 
        pedido= cursor.fetchone()
        conexion.close()
        if pedido:
           
            print("Ese pedido si existe :", pedido)
            return pedido
        else:
            messagebox.showwarning("Error", "Ese pedido no existe tibio.")
            return None
        
    # Método para consultar todos los pedidos
    def consultarPedido(self):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, departamento, producto, cantidad, fecha, status FROM pedidos")
            pedido = cursor.fetchall()
            return pedido
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al consultar Pedidos: {e}")
        finally:
            if conexion:
                conexion.close()
    
  
    def actualizarPedido(self, id, departamento, producto, cantidad, fecha, status):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
         
            datos = (departamento, producto, cantidad, fecha, status, id)
            sqlupdate = "UPDATE pedidos SET departamento = ?, producto = ?, cantidad = ?, fecha = ?, status = ? WHERE id = ?"
            cursor.execute(sqlupdate, datos)
            conexion.commit()
        except Exception as e:
            messagebox.showerror("Error al actualizar", f"Error: {e}")
        finally:
            conexion.close()
            messagebox.showinfo("Actualización", "Pedido actualizado con éxito")
    
    def eliminarPedido(self, id):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            sqldelete = "DELETE FROM pedidos WHERE id = ?"
            cursor.execute(sqldelete, (id,))
            conexion.commit()
        except Exception as e:
            messagebox.showerror("Error al eliminar", f"Error: {e}")
        finally:
            conexion.close()
            messagebox.showinfo("Eliminación", "Pedido eliminado con éxito")




 