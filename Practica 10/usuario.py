class Usuario:
    
    def _init_(self, id_usuario, nombre, apellido_p, apellido_m, correo, contrasena):
        self.__id = id_usuario
        self.__nombre = nombre
        self.__apellido_p = apellido_p
        self.__apellido_m = apellido_m
        self.__correo = correo
        self.__contrasena = contrasena
        
    # Getters
    def get__id(self):
        return self.__id
    
    def get__nombre(self):
        return self.__nombre

    def get__apellido_p(self):
        return self.__apellido_p

    def get__apellido_m(self):
        return self.__apellido_m

    def get__correo(self):
        return self.__correo

    def get__contrasena(self):
        return self.__contrasena

    # Setters
    def set__id(self, valor):
        self.__id = valor

    def set__nombre(self, valor):
        self.__nombre = valor

    def set__apellido_p(self, valor):
        self.__apellido_p = valor

    def set__apellido_m(self, valor):
        self.__apellido_m = valor

    def set__correo(self, valor):
        self.__correo = valor

    def set__contrasena(self, valor):
        self.__contrasena = valor