'''Escribir un programa que solicite un entero X, introducido por el usuario y después
muestre en pantalla la suma de todos los enteros desde 1 hasta X .'''

# Solicitamos al usuario un número entero
numero = int(input("Por favor, introduzca un número entero: "))

# Calculamos la suma de todos los enteros desde 1 hasta el número dado
suma = sum(range(1, numero + 1))

# Mostramos la suma por pantalla
print("La suma de todos los enteros desde 1 hasta", numero, "es:", suma)

