class CRUD:
    
    def _init_(self):
        self.usuarios = []
        
    def crear_usuario(self, usuario):
        self.usuarios.append(usuario)
        return usuario

    def consultar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.get__id() == id_usuario:
                return usuario
        return None

    def actualizar_usuario(self, id_usuario, nombre=None, apellido_p=None, apellido_m=None, correo=None, contrasena=None):
        usuario = self.consultar_usuario(id_usuario)
        if usuario is not None:
            if nombre is not None:
                usuario.set__nombre(nombre)
            if apellido_p is not None:
                usuario.set__apellido_p(apellido_p)
            if apellido_m is not None:
                usuario.set__apellido_m(apellido_m)
            if correo is not None:
                usuario.set__correo(correo)
            if contrasena is not None:
                usuario.set__contrasena(contrasena)
            return True
        return False

    def eliminar_usuario(self, id_usuario):
        usuario = self.consultar_usuario(id_usuario)
        if usuario is not None:
            self.usuarios.remove(usuario)
            return True
        return False