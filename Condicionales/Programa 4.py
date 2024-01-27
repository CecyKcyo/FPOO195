'''Codifica un programa que solicite una cadena de caracteres e imprima como
resultado si la cadena es palíndromo o no'''
cadena = input("Introduce una cadena de caracteres: ")

if cadena == cadena[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")