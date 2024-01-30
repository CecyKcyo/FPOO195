'''Imprime un árbol de navidad formado con Asteriscos haciendo uso del while,
Solicitando al usuario la cantidad de * de la base (img 3)'''
base = int(input("Introduce la cantidad de asteriscos de la base del árbol: "))
altura = base // 2 + 1

for i in range(1, altura + 1):
    espacio = altura - i
    print(" " * espacio + "*" * (2*i - 1))
