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