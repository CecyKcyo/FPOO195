class Usuario:
    def __init__(self, id, contraseña, correo):
        self._id = id
        self._contraseña = contraseña
        self._correo = correo

    def obtener_id(self):
        return self._id

    def obtener_contraseña(self):
        return self._contraseña

    def obtener_correo(self):
        return self._correo

    def establecer_contraseña(self, contraseña):
        self._contraseña = contraseña

    def establecer_correo(self, correo):
        self._correo = correo
