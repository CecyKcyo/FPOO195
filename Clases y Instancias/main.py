# Archivo main.py
from Personaje import *
from Armas import *

#Solicitar datos Spartan
print("===== Datos del Heroe =====")
nombreS = input("Escribe el nombre de tu Spartan: ")
especieS = input("Escribe la especie de tu Spartan: ")
alturaS = float(input("Escribe la altura de tu Spartan: "))

#Solicitar datos del Nemesis
print("===== Datos del villano =====")
nombreN = input("Escribe el nombre del Nemesis: ")
especieN = input("Escribe la especie del Nemesis: ")
alturaN = float(input("Escribe la altura del Nemesis: "))

#Creamos el objeto de la clase personaje       
spartan = Personaje(especieS, nombreS, alturaS)
Nemesis = Personaje(especieN, nombreN, alturaN)
Arma = Armas()
print("")

#Usamos los atributos Spartan
print("===== El objeto Spartan contiene ======")
print(spartan.get__nombre())
print(spartan.get__especie())
print(spartan.get__altura())
print("")

#Usamos los atributos Nemesis
print("===== El objeto Nemesis contiene ======")
print(Nemesis.get__nombre())
print(Nemesis.get__especie())
print(Nemesis.get__altura())
print("")

#Usamos los metodos del Spartan
print("===== Metodos del objeto spartan =====")
spartan.correr(False)
spartan.lanzarGranada()
print("")

#Usamos los metodos del Nemesis
print("===== Metodos del objeto Nemesis =====")
Nemesis.correr(True)
Nemesis.lanzarGranada()
print("")


#Usamos los metodos del Arma
Arma.seleccionarArma(spartan.get__nombre())
Arma.recargarArma(65)