'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.'''

numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")