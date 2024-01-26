'''Crea un programa que pregunte al usuario por el número de horas trabajadas y el
coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''
#Leemos un primer número
horas=float(input("Ingresa las horas trabajadas: "))

#Leemos un segundo número
pagoxhora=float(input("Por favor ingrese el precio pagado por hora: "))


# Mostramos el resultado de la suma
print(horas, "*", pagoxhora, "= $", horas * pagoxhora)