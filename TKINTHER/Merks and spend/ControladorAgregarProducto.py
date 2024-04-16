from tkinter import messagebox
import sqlite3

class Controlador:
    # Método para establecer conexión con la base de datos SQLite
    def conexion(self):
        try:
            conex = sqlite3.connect("D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/bdMerks.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar con la base de datos.")

    # Método para insertar un nuevo producto en la base de datos
    def insertProducto(self, nombre, cantidad, precio):
        conexion = self.conexion()
        if (nombre == "" or cantidad == "" or precio == ""):
            messagebox.showwarning("Cuidado", "Llena todos los campos del producto")
            conexion.close()
        else:
            cursor = conexion.cursor()
            datos = (nombre, cantidad, precio)
            sqlinsert = "INSERT INTO productos(nombre, cantidad, precio) VALUES (?, ?, ?)"
            cursor.execute(sqlinsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Producto agregado exitosamente")

    def consultarProductoPorID(self, id_producto):
        conexion = self.conexion()
        cursor = conexion.cursor()
        sqlconsulta = "SELECT id, nombre, cantidad, precio FROM productos WHERE id = ?"
        cursor.execute(sqlconsulta, (id_producto,))
        producto = cursor.fetchone()
        conexion.close()
        if producto:
            print("Producto encontrado:", producto)
            return producto
        else:
            messagebox.showwarning("Error", "Ese producto no existe.")
            return None

    # Método para consultar todos los productos
    def consultarProductos(self):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, cantidad, precio FROM productos")
            productos = cursor.fetchall()
            return productos
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al consultar productos: {e}")
        finally:
            if conexion:
                conexion.close()

    def actualizarProducto(self, id_producto, nombre, cantidad, precio):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            datos = (nombre, cantidad, precio, id_producto)
            sqlupdate = "UPDATE productos SET nombre = ?, cantidad = ?, precio = ? WHERE id = ?"
            cursor.execute(sqlupdate, datos)
            conexion.commit()
        except Exception as e:
            messagebox.showerror("Error al actualizar", f"Error: {e}")
        finally:
            conexion.close()
            messagebox.showinfo("Actualización", "Producto actualizado con éxito")

    def eliminarProducto(self, id_producto):
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            sqldelete = "DELETE FROM productos WHERE id = ?"
            cursor.execute(sqldelete, (id_producto,))
            conexion.commit()
        except Exception as e:
            messagebox.showerror("Error al eliminar", f"Error: {e}")
        finally:
            conexion.close()
            messagebox.showinfo("Eliminación", "Producto eliminado con éxito")
