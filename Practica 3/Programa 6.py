'''Crea un programa que pida al usuario que introduzca una frase en y muestre en
pantalla la frase invertida.'''

# Solicitamos al usuario una frase
frase = input("Por favor, introduzca una frase: ")

# Invertimos la frase utilizando algo llamado slicing con paso negativo
frase_invertida = frase[::-1]

# Mostramos la frase invertida por pantalla
print("La frase invertida es:", frase_invertida)