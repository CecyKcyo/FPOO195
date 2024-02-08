'''Crea un programa que usando bucles nos permita pedir un numero par comprendido entre 200 y 400 y nos muestre todos los numeros pares comprendidos entre el 
numero facilitado y 400. Por ejemplo si el numero facilitado es "392", nos debera mostarr (392, 396, 398, 400)'''
numero=int(input("Por favor introcuce un numero par entre 200 y 4000"))

while numero % 2 !=0 or numero < 200 or numero > 400:
    numero=int(input("El numero no es un par entre 200 y 400"))
    
    print(f"Los numeros pares entre{numero} y 400: son:")
while numero <= 400:
    print(numero, end=", ")
    # print(", ".join(i)) 

    numero +=2