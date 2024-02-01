'''Imprime un árbol de navidad formado con Asteriscos haciendo uso del while,
Solicitando al usuario la cantidad de * de la base (img 3)'''
def imprimir_arbol_navidad(base):
    altura = base + 1
    
  
    i = 1
    while i < altura:
        espacios = altura - i - 1
        asteriscos = 2 * i - 1
        print(' ' * espacios + '*' * asteriscos)
        i += 1

base = int(input("Ingrese la cantidad de asteriscos en la base del árbol de Navidad: "))


imprimir_arbol_navidad(base)
