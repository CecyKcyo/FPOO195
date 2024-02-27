# Definición de la clase Personaje
class Personaje:
    
    # Constructor de la clase Personaje. Este método se llama automáticamente al crear un nuevo objeto.
    # Inicializa los atributos del personaje con los valores proporcionados.
    def __init__(self, esp, nom, alt):
        # Asignación de valores a los atributos de instancia del objeto.
        self.especie = esp  # Asigna el valor de 'esp' al atributo 'especie'.
        self.nombre = nom  # Asigna el valor de 'nom' al atributo 'nombre'.
        self.altura = alt  # Asigna el valor de 'alt' al atributo 'altura'.
    
    # Método de instancia 'correr' que define una acción del personaje.
    def correr(self, estado):
        if(estado):  # Si 'estado' es True, el personaje puede correr.
            # Imprime que el personaje está corriendo.
            print("El personaje "+ self.nombre +" esta corriendo")
        else:  # Si 'estado' es False, el personaje no puede correr (está muerto).
            # Imprime que el personaje está muerto y no puede correr.
            print("El personaje "+ self.nombre +" esta muerto")
    
    # Método de instancia 'lanzarGranada' que define otra acción del personaje.
    def lanzarGranada(self):
        # Imprime que el personaje ha lanzado una granada.
        print(self.nombre+" Pego una granada")
