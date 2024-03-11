class Serie:
    def __init__(self, titulo="", genero="", calificacion=0):
        self.__titulo = titulo
        self.__horas_estimadas = 10
        self.__status = "Sin reproducir"
        self.__genero = genero
        self.__calificacion = calificacion

    def reproducir(self):
        return f"Reproduciendo {self.__titulo}"

    def agregar_a_mi_lista(self):
        return f"{self.__titulo} agregado a mi lista"

    def marcar_como_completada(self):
        self.__status = "Completada"

    def calificar(self, calificacion):
        self.__calificacion = calificacion

    # Métodos get y set para cada atributo
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def horas_estimadas(self):
        return self.__horas_estimadas

    @property
    def status(self):
        return self.__status

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def calificacion(self):
        return self.__calificacion

    @calificacion.setter
    def calificacion(self, calificacion):
        self.__calificacion = calificacion
