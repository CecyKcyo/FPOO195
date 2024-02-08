'''Escriba un programa que pida al usuario dos palabras por consola, y que indique cual de ellas es la mas larga y por cuantas letras lo es '''

palabra1  = input("Ingrese la primera palabra: ")
palabra2  = input("Ingrese la primera palabra: ")

longitud_palabra1 = len(palabra1)
longitud_palabra2 = len(palabra2)

if longitud_palabra1 > longitud_palabra2:
    print(f"{palabra1} es más larga que {palabra2} por {longitud_palabra1 - longitud_palabra2} letras.")
elif longitud_palabra2 > longitud_palabra1:
    print(f"{palabra2} es más larga que {palabra1} por {longitud_palabra2 - longitud_palabra1} letras.")
else:
    print("Ambas palabras tienen la misma longitud.")

