'''Codifica un programa que pregunte el nombre completo del usuario en la consola y
después muestre por pantalla el nombre completo del usuario tres veces, una con
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
primera letra del nombre y de los apellidos en mayúscula. El usuario puede
introducir su nombre combinando mayúsculas y minúsculas como quiera.'''

def mostrar_nombres(nombre, apellido):
    # Convertir el nombre y apellidos a minúsculas
    nombre_minusculas = nombre.lower()
    apellido_minusculas = apellido.lower()

    # Convertir el nombre y apellidos a mayúsculas
    nombre_mayusculas = nombre.upper()
    apellido_mayusculas = apellido.upper()

    # Capitalizar la primera letra del nombre y apellido
    nombreL = nombre[0]
    apellido_mayusculas = apellido.upper()

    # Imprimir los nombres
    print("1:", nombre_minusculas, apellido_minusculas)
    print("2:", nombre_mayusculas, apellido_mayusculas)
    print("3:", nombreL, apellido_mayusculas)


# Pedir al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Pedir al usuario que ingrese sus apellidos
apellido = input("Ingrese su apellido: ")

# Llamar a la función para mostrar los nombres
mostrar_nombres(nombre, apellido)
