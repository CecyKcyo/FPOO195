# Archivo personaje.py

class Personaje:
    
    #atributo de personaje
    #Declaramos el constructor
    
    def _init_(self,esp,nom,alt):

        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
        
    def get__especie(self):
        return self.__especie
    
    def get__nombre(self):
        return self.__nombre
    
    def get__altura(self):
        return self.__altura
    
    def set__especie(self, __especie):
        self.__especie = __especie
       
    def set__nombre(self, __nombre):
        self.__nombre = __nombre 
        
    def set__altura(self, __altura):
        self.__altura = __altura
    
    
    #Metodos del personaje
    def correr(self, __estado):
        if(__estado):
            print("El personaje"+ self.__nombre+" está corriendo")
        else:
            print("El personaje "+ self.__nombre+" está muerto")
            
    def lanzarGranada(self):
        print(self.__nombre + " Pegó una granada")