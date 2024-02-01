'''Escribir una función que convierta un número decimal en binario y
otra que convierta un número binario en decimal.'''

def d_b(decimal):
    return bin(decimal)[2:]
def b_d(binario):
    return int(binario, 2)
opcion=input("¿qué deseas hacer? (Op: 1.Decimal-binario 2.Binario-decimal)")
if opcion=="1":
    decimal=int(input("Ingrese un numero decimal:"))
    binario=d_b(decimal)
    print("Tu numero en binario es:", binario)
elif opcion=="2":
    binario=input("ingrese un numero binario")
    decimal=b_d(binario)
    print("Tu binario es igual a:", decimal)
else:
    print("opcion invalida")