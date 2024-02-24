from Personaje import *
from Armas import *

#instancia creamos eo objeto de la clase personsaje   
spartan=Personaje()
Arma = Armas()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Usamos los metodos del Spartan

spartan.correr(False)
spartan.lanzarGranada()


#Usamos los metodos de arma
Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma()