
class Personaje:
# Definimos nuestra clase

    # Atributos de nuestro personaje
    especie= "Humano"
    nombre= "John"
    altura= 2.18 
    #Metodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje "+self.nombre+"Esta corriendo")
            
        else:
            print("El personaje "+self.nombre+"Esta muerto")

    def lanzarGranada(self):
        print(self.nombre+" Pego una granada")
        
    
     
    
