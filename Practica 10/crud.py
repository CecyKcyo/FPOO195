from usuario import Usuario 

class CRUD:
  
    def __init__(self):
        
        # Inicializa una lista vacía para almacenar los usuarios
        self._usuarios = []

    def crear_usuario(self, usuario):
       
        self._usuarios.append(usuario)

    def editar_usuario(self, id, nombre, edad, direccion, contraseña, correo):
       
        for usuario in self._usuarios:
            if usuario.obtener_id() == id:
                usuario.establecer_nombre(nombre)
                usuario.establecer_edad(edad)
                usuario.establecer_direccion(direccion)
                usuario.establecer_contraseña(contraseña)
                usuario.establecer_correo(correo)
                break  # Sale del bucle una vez que se actualiza el usuario

    def eliminar_usuario(self, id):
        
        for usuario in self._usuarios:
            if usuario.obtener_id() == id:
                self._usuarios.remove(usuario)
                break  # Sale del bucle una vez que se elimina el usuario

    def consultar_usuario(self):
        
        return self._usuarios
