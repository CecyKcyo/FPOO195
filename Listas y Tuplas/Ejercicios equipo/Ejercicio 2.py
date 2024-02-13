'''Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
al 20, con la lista llena el usuario podrá
a. Contar número repetidos
b. Eliminar numero repetidos
c. Remplazar los repetidos con 0'''
import random

# Función para llenr la lista con valores aleatorios 
def llenar_lista():
    return [random.randint(10, 20) for _ in range(30)]

# Función para contar repetidos repetidos
def contar_repetidos(lista):
    repetidos = {}
    for numero in lista:
        if lista.count(numero) > 1:
            repetidos[numero] = lista.count(numero)
    return repetidos

# Función para eliminar num repetidos
def eliminar_repetidos(lista):
    return list(set(lista))

# Función para reemplazar num repetidos con 0
def reemplazar_repetidos_con_cero(lista):
    repetidos = [numero for numero in lista if lista.count(numero) > 1]
    return [0 if numero in repetidos else numero for numero in lista]

# Función para mostrar el menú y procesar la opción seleccionada
def procesar_lista():
    lista = llenar_lista()
    print("Lista generada:", lista)
    
    while True:
        print("\nMenú:")
        print("a. Contar números repetidos")
        print("b. Eliminar números repetidos")
        print("c. Reemplazar los repetidos con 0")
        print("d. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == 'a':
            repetidos = contar_repetidos(lista)
            for numero, cantidad in repetidos.items():
                print(f"El número {numero} se repite {cantidad} veces.")
        elif opcion == 'b':
            lista = eliminar_repetidos(lista)
            print("Lista sin repetidos:", lista)
        elif opcion == 'c':
            lista = reemplazar_repetidos_con_cero(lista)
            print("Lista con repetidos reemplazados por 0:", lista)
        elif opcion == 'd':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

if __name__ == "__main__":
    procesar_lista()
