from ViajeroFrecuente import  ViajeroFrecuente
from ManejadorViajeros import ManejadorViajero

def test():
    print("TEST:")      #Crea un objeto de la clase ViajeroFrecuente y la muestra para verificar que se creo correctamente
    control1 = ViajeroFrecuente(5, 43340662, "Nicolas", "Garcia", 6500.89)
    print(control1)


if __name__ == '__main__':
    test()
    lista = ManejadorViajero()      #Crea objeto de la clase manejador
    lista.testViajeros()            #Abre el archivo y crea instancias de la clase ViajeroFrecuente para almacenar en la lista
    indice = lista.buscarViajero(input("Ingrese numero de viajero: "))  
    if indice != None:      #Verifica que el indice de Viajero ingresado corresponda
        opcion = int(input("MENU:\nOpción 1: Consultar cantidad de Millas\nOpción 2: Acumular Millas\nOpcion 3: Canjear Millas\nOpcion 4: Salir\nEligir opción: "))
        while opcion != 4:
            if opcion == 1:     #Consulta cantidad de millas
                print('El Viajero tiene {} millas'.format(lista.getMillasdeViajero(indice)))
            elif opcion == 2:      #Realiza acumulacion de millas
                millasAacumular = int(input("Ingrese cantidad de millas para acumular: "))
                lista.acumularMillas(indice, millasAacumular)
                print('El Viajero tiene {} millas'.format(lista.getMillasdeViajero(indice)))
            elif opcion == 3:       #Realiza canjeo de millas
                millasAcanjear = int(input("Ingrese cantidad de millas a canjear: "))
                lista.canjearMillas(indice, millasAcanjear)
                print('El Viajero tiene {} millas'.format(lista.getMillasdeViajero(indice)))
            else:
                print("Opción ingresada no corresponde")
            opcion = int(input("MENU:\nOpción 1: Consultar cantidad de Millas\nOpción 2: Acumular Millas\nOpcion 3: Canjear Millas\nOpcion 4: Salir\nEligir opción: "))
    else:
        print("Número de viajero no corresponde")
    
