from usuario import Usuario

class CRUD:
    def __init__(self):
        self._usuarios = []

    def crear_usuario(self, usuario):
        self._usuarios.append(usuario)

    def editar_usuario(self, id, contraseña, correo):
        for usuario in self._usuarios:
            if usuario.obtener_id() == id:
                usuario.establecer_contraseña(contraseña)
                usuario.establecer_correo(correo)
                break

    def eliminar_usuario(self, id):
        for usuario in self._usuarios:
            if usuario.obtener_id() == id:
                self._usuarios.remove(usuario)
                break

    def consultar_usuario(self):
        return self._usuarios

    def buscar_usuario_por_correo(self, correo):
        for usuario in self._usuarios:
            if usuario.obtener_correo() == correo:
                return usuario
        return None
    
   