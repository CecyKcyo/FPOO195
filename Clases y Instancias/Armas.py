class Armas:
    
    def seleccionarArma(self, nombre):
        seleccion=int(input("Seleccionar el arma: \n 1 =Rifle de asalto \n2=Espada de energía\n3=Rifle M392"))
        if(seleccion == 1):
            print("El rifle de asalto asignado a "+ nombre)
            print("Municion 7.62*52 mm, sin mira")
        if(seleccion == 2 ):
            print("La espada de nergía  asignado a "+ nombre)
            print("Arma creada por los Shangheili")
        if(seleccion == 3):
            print("El rifle M392 asignado a "+ nombre)
            print("Municion 7.62*52 mm, con mira")
        
    def recargarArma(self, municion):
        cargador= 25
        cargador=cargador+municion
        print("Arma recargada al "+ str(cargador)+"%")