
import random

def generar_matricula(nombre, apellido_paterno, apellido_materno, año_curso, año_nacimiento, carrera):
    # Obtener las partes de la matrícula
    tres_letras_carrera = carrera[:3].upper()
    dos_digitos_año2 = año_curso[-2:]
    dos_digitos_año = año_nacimiento[-2:]
    primera_letra_nombre = nombre[0].upper()
    tres_letras_apellido_paterno = apellido_paterno[:3].upper()
    tres_letras_apellido_materno = apellido_materno[:3].upper()
    tres_digitos_aleatorios = ''.join(random.choices('0123456789', k=3))

    # Unir las partes para formar la matrícula
    matricula = f"{tres_letras_carrera}{dos_digitos_año2}{dos_digitos_año}{primera_letra_nombre}{tres_letras_apellido_paterno}{tres_letras_apellido_materno}{tres_digitos_aleatorios}"

    return matricula
