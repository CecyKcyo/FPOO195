'''Escribir un programa que almacene la cadena de caracteres una contraseña en
una variable, después que solicite al usuario una contraseña e imprima en
pantalla si la contraseña introducida por el usuario coincide con la guardada en
la variable sin tener en cuenta mayúscula y minúscula.'''

contraseña_guardada = "contraseña"  # Cambiar por la contraseña deseada

contraseña_usuario = input("Introduce la contraseña: ")

if contraseña_usuario.lower() == contraseña_guardada.lower():
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta.")