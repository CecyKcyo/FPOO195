class Usuario:
    # Define una clase llamada Usuario para representar usuarios

    def __init__(self, id, nombre, edad, direccion, contraseña, correo):
        
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._direccion = direccion
        self._contraseña = contraseña
        self._correo = correo

    def obtener_id(self):
        # obtener el ID del usuario
        return self._id

    def obtener_nombre(self):
        # obtener el nombre del usuario
        return self._nombre

    def obtener_edad(self):
        # obtener la edad del usuario
        return self._edad

    def obtener_direccion(self):
        # obtener la dirección del usuario
        return self._direccion

    def obtener_contraseña(self):
        # obtener la contraseña del usuario
        return self._contraseña

    def obtener_correo(self):
        # obtener el correo del usuario
        return self._correo

    def establecer_nombre(self, nombre):
        # establecer el nombre del usuario
        self._nombre = nombre

    def establecer_edad(self, edad):
        # establecer la edad del usuario
        self._edad = edad

    def establecer_direccion(self, direccion):
        # establecer la dirección del usuario
        self._direccion = direccion

    def establecer_contraseña(self, contraseña):
        # establecer la contraseña del usuario
        self._contraseña = contraseña

    def establecer_correo(self, correo):
        # establecer el correo del usuario
        self._correo = correo
