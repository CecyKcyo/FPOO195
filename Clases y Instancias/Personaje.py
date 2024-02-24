# Definimos nuestra clase
class Personaje:
    # Atributos de nuestro personaje
    especie= "Humano"
    nombre= "John"
    altura= 2.18 
    #Metodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje"+self.nombre+"Esta corriendo")
            
        else:
            print("El personaje"+self.nombre+"Esta muerto")
             
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada")
        
    def recargarGranada(self, municion):
        cargador= 25
        cargador=cargador+municion
        print("Arma recargada al"+ str(cargador)+"%")
     
    #instancia creamos eo objeto de la clase personaje   
spartan=Personaje()
print(spartan.nombre)
print(spartan.especie)
print(spartan.recargarGranada)