'''Escribir una función que calcule el total de una factura tras aplicarle
el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
IVA a aplicar, y devolver el total de la factura. Si se invoca la función
sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''

def calcular_factura(cantidad_s_iva, porcentaje_iva=21):
    
    total=cantidad_s_iva + (cantidad_s_iva*porcentaje_iva/100)

    return total

cantidad_s_iva=float(input("ingrese la cantidad sin iva:"))
porcentaje_iva=float(input("Ingrese el porcentaje del iva:")or 21)
total=calcular_factura(cantidad_s_iva, porcentaje_iva)
print("El total de tu pago es:", total)
    
