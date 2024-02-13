
'''Crea un programa usando funciones y lo que necesites para que el usuario inserte
N números en una Tupla, después de la captura debe desplegar el siguiente menú
funcional
1. Sumatoria de los elementos de la lista
2. Numero mayor de la lista
3. Numero menor de la lista
4. Promedio
5. Moda: es el valor que más se repite de un conjunto de datos
6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
conjunto de datos'''
def capturar_numeros():
    # Función para capturar números ingresados por el usuario y formar una tupla
    n = int(input("Ingrese la cantidad de números que desea agregar a la tupla: "))
    # Solicita al usuario la cantidad de números
    numeros = tuple(float(input(f"Ingrese el número {i+1}: ")) for i in range(n))
    # Captura los números ingresados por el usuario y los convierte en una tupla
    return numeros

def sumatoria(lista):
    # Función para calcular la sumatoria de los elementos de la lista
    return sum(lista)

def numero_mayor(lista):
    # Función para encontrar el número mayor de la lista
    return max(lista)

def numero_menor(lista):
    # Función para encontrar el número menor de la lista
    return min(lista)

def promedio(lista):
    # Función para calcular el promedio de los elementos de la lista
    return sum(lista) / len(lista)

def moda(lista):
    # Función para encontrar la moda, es decir, el valor que más se repite en la lista
    conteo = {}
    for numero in lista:
        conteo[numero] = conteo.get(numero, 0) + 1
    max_repeticiones = max(conteo.values())
    modas = [numero for numero, repeticiones in conteo.items() if repeticiones == max_repeticiones]
    return modas

def rango(lista):
    # Función para calcular el rango, es decir, la diferencia entre el valor máximo y mínimo de la lista
    return max(lista) - min(lista)

def menu_operaciones(lista):
    # Función que muestra un menú de opciones y permite al usuario seleccionar una operación a realizar en la lista de números
    while True:
        print("\nSeleccione una opción:")
        print("1. Sumatoria de los elementos de la lista")
        print("2. Numero mayor de la lista")
        print("3. Numero menor de la lista")
        print("4. Promedio")
        print("5. Moda")
        print("6. Rango")
        print("7. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            print("Sumatoria de los elementos de la lista:", sumatoria(lista))
        elif opcion == '2':
            print("Número mayor de la lista:", numero_mayor(lista))
        elif opcion == '3':
            print("Número menor de la lista:", numero_menor(lista))
        elif opcion == '4':
            print("Promedio de los elementos de la lista:", promedio(lista))
        elif opcion == '5':
            print("Moda de la lista:", moda(lista))
        elif opcion == '6':
            print("Rango de la lista:", rango(lista))
        elif opcion == '7':
            break
        else:
            print("Opción no válida")

def main():
    # Función principal del programa, pues capturamos los numeros de la terminal
    numeros = capturar_numeros()
    # Captura los números ingresados por el usuario
    menu_operaciones(numeros)
    # Llama a la función del menú de operaciones, pasando la lista de números ingresada por el usuario

if __name__ == "__main__":
    # Verifica si el programa está siendo ejecutado como un script principal
    main()
    # Si es así, llama a la función principal para iniciar la ejecución del programa
