#Practica2: Sintaxis python 
#1 comentarios 
#soy un comentador de lineas
'''Soy un 
comentador 
de varias 
lineas 
'''




#Cadenas 
"""print('Soy una cadena')
print("Soy otra cadena")"""

a='Mi banda es \n favorita es'
b="Es marrano"
print(a+b)
print(a, b)
#Hola
#contar caracteres 
print(len(a))
print(b[2:5])
print(b[:5])
print(b[2:])


# 3 variables 
x=int(3)
y=str("3")
z=float(3.2)

print(type(x))
print(type(y))
print(type(z))

import random
numero=random.randrange(1, 15)
print(numero)

#4. Solicitud de datos
var1=input("introduce cualquier dato")
var2=str(input("introduce cadenas"))
var3=int(input("introduce solo enteros"))
var4=input("introduce numeros decimales ")

print(var1, var2, var3)

#5 Booleans, operadores de comparacion y logicos
"""print(10>9)
print(10==9)
print(10<9)
print(10>=9)
print(10<=9)
print(10!=9)"""
#Para binarias 
x=1
print(x<5 and x<10)
print(x<5 or x<10)
print(not (x<5 and x<10)) 


print(x<5 & x<10)
print(x<5 | x<10)
print(not (x<5 & x<10))
