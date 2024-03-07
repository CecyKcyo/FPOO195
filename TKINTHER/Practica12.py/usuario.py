class Usuario:
    # Define una clase llamada Usuario para representar usuarios

    def __init__(self, id,  contraseña, correo):
        
        self._id = id
        self._contraseña = contraseña
        self._correo = correo

    def obtener_id(self):
        # obtener el ID del usuario
        return self._id

    
    def obtener_contraseña(self):
        # obtener la contraseña del usuario
        return self._contraseña

    def obtener_correo(self):
        # obtener el correo del usuario
        return self._correo

    

    def establecer_contraseña(self, contraseña):
        # establecer la contraseña del usuario
        self._contraseña = contraseña

    def establecer_correo(self, correo):
        # establecer el correo del usuario
        self._correo = correo
