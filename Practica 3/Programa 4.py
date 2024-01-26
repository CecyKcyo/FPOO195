'''Codifica un programa que pregunte el nombre del usuario y después de que el
usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
<NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
que tienen el nombre.'''

# Solicitamos al usuario su nombre
nombre_usuario = input("Por favor, introduzca su nombre: ")

# Contamos el número de letras en el nombre del usuario
numero_letras = len(nombre_usuario)

# Mostramos por pantalla el resultado
print(nombre_usuario.upper(), "tiene", numero_letras, "letras.")

