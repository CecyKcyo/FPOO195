# Archivo Armas.py
class Armas: 
    
    def seleccionarArma(self, get__nombre):
        seleccion = int(input("Seleccionar el arma: \n 1 = Rifle de asalto\n 2 = Espada de energia \n 3 = Rifle M392"))
        print("")
        
        if(seleccion == 1):
            print("Rifle de asalto asignado a " + get__nombre())
            print("Municiones 7.62 * 52 mm, sin mira")

        if(seleccion == 2):
            print("Espada de energia asignada a " + get__nombre())
            print("Arma creada por los Shagheili")
        
        if(seleccion == 3):
            print("Rifle M392 asignado a " + get__nombre())
            print("Municiones 7.62 * 52 mm, con mira")
            
    
    def recargarArma(self, municion):
        cargador= 25
        cargador=cargador+municion
        print("Arma recargada al "+ str(cargador)+"%")