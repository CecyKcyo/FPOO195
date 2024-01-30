'''Escriba un programa que administre una cuenta bancaria, usando una bitácora
de operaciones. (img 2)
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50
D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos
Introducir una línea vacía indica que ha finalizado la bitácora e imprime el saldo
final'''
saldo = 0
while True:
    operacion = input("Introduce la operación (D para depósito, R para retiro): ")
    if operacion == "":
        break
    monto = float(input("Introduce el monto: "))
    if operacion == "d":
        saldo += monto
    elif operacion == "r":
        saldo -= monto
    else:
        print("Operación no válida.")
    print(f"Saldo actual: {saldo}")
print(f"Saldo final: {saldo}")
