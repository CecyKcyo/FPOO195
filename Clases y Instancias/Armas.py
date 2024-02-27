# Definición de la clase Armas.
class Armas:
    # Método para seleccionar un arma para un personaje.
    def seleccionarArma(self, nombre):
        # Solicita al usuario elegir una opción de arma mediante input y lo convierte a entero.
        seleccion = int(input("Selecciona el arma:\n 1 = Rifle de asalto\n 2 = Espada de energia\n 3 = Rifle M392\n"))
        
        # Condicionales que verifican la elección del usuario y muestran el arma seleccionada junto con su descripción.
        if(seleccion == 1):
            # Información del Rifle de asalto.
            print("Rifle de asalto asignado a "+ nombre)
            print("Municiones 7.62 * 52mm, sin mira")
            
        if(seleccion == 2):
            # Información de la Espada de energía.
            print("Espada de energia asignada a "+ nombre)
            print("Arma creada por los Shagheili")
        
        if(seleccion == 3):
            # Información del Rifle M392.
            print("Rifle M392 asignado a "+ nombre)
            print("Municiones 7.62 * 52mm, con mira")
        
    # Método para recargar el arma con una cantidad de munición especificada por el usuario.
    def recargarArma(self, municion):
        # Inicializa la cantidad de munición en el cargador.
        cargador = 25
        # Suma la munición especificada al cargador.
        cargador = cargador + municion
        # Imprime el porcentaje al cual ha sido recargado el arma, asumiendo que el 100% es la capacidad total del cargador.
        # Aquí hay un pequeño error conceptual, ya que se suman unidades de munición, pero se indica el resultado como un porcentaje.
        print("arma recargada al "+ str(cargador)+ "%")
