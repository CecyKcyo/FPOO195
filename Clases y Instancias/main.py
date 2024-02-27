# Importación de clases desde otros módulos/archivos.
from Personaje import *  # Importa todas las clases y funciones definidas en el módulo 'Personaje'.
from Armas import *  # Importa todas las clases y funciones definidas en el módulo 'Armas'.

# Solicitar datos del Spartan (héroe).
print("===== Datos de Heroe =====")
nombreS = input("Escribe el nombre de tu Spartan ")  # Solicita y almacena el nombre del Spartan.
especieS = input("Escribe la especie de tu Spartan ")  # Solicita y almacena la especie del Spartan.
alturaS = float(input("Escribe la altura de tu Spartan "))  # Solicita, convierte a float y almacena la altura del Spartan.

# Solicitar datos del Nemesis (villano).
print("===== Datos de Villano =====")
nombreN = input("Escribe el nombre de tu Nemesis ")  # Solicita y almacena el nombre del Nemesis.
especieN = input("Escribe la especie de tu Nemesis ")  # Solicita y almacena la especie del Nemesis.
alturaN = float(input("Escribe la altura de tu Nemesis "))  # Solicita, convierte a float y almacena la altura del Nemesis.

# Creación de objetos de la clase Personaje para el Spartan y el Nemesis.
spartan = Personaje(especieS, nombreS, alturaS)  # Crea un objeto 'spartan' con los datos recogidos.
Nemesis = Personaje(especieN, nombreN, alturaN)  # Crea un objeto 'Nemesis' con los datos recogidos.

# Creación de un objeto de la clase Armas.
Arma = Armas()  # Crea un objeto 'Arma' de la clase 'Armas'.

# Impresión de los atributos del objeto 'spartan'.
print(spartan.nombre)  # Imprime el nombre del Spartan.
print(spartan.especie)  # Imprime la especie del Spartan.
print(spartan.altura)  # Imprime la altura del Spartan.

# Impresión de los atributos del objeto 'Nemesis'.
print(Nemesis.nombre)  # Imprime el nombre del Nemesis.
print(Nemesis.especie)  # Imprime la especie del Nemesis.
print(Nemesis.altura)  # Imprime la altura del Nemesis.

# Uso de métodos del objeto 'spartan'.
spartan.correr(False)  # Ejecuta el método 'correr' del Spartan, indicando que no puede correr (posiblemente está muerto).
spartan.lanzarGranada()  # Ejecuta el método 'lanzarGranada' del Spartan.

# Uso de métodos del objeto 'Nemesis'.
Nemesis.correr(False)  # Ejecuta el método 'correr' del Nemesis, indicando que no puede correr (posiblemente está muerto).
Nemesis.lanzarGranada()  # Ejecuta el método 'lanzarGranada' del Nemesis.

# Uso de métodos del objeto 'Arma'.
Arma.seleccionarArma(spartan.nombre)  # Selecciona un arma para el Spartan.
Arma.recargarArma(65)  # Recarga el arma seleccionada con 65 unidades de munición.
