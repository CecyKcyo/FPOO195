'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el número
introducido. (img 1)'''
def imprimir_triangulo_rectangulo(numero):
    for i in range(1, numero + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

try:
    numero = int(input("Ingrese un número entero: "))
    imprimir_triangulo_rectangulo(numero)
except ValueError:
    print("Error: Por favor ingrese un número entero válido.")
