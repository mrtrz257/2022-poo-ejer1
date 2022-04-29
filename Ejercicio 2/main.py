from ManejadorViajeros import ManejadorViajero

if __name__ == '__main__':
    lista = ManejadorViajero()
    lista.testViajeros()
    indice = lista.buscarViajero(input("Ingrese numero de viajero: "))
    if indice != None:
        opcion = int(input("MENU:\nOpción 1: Consultar cantidad de Millas\nOpción 2: Acumular Millas\nOpcion 3: Canjear Millas\nOpcion 4: Salir\nEligir opción: "))
        while opcion != 4:
            if opcion == 1:
                print(lista.getMillasdeViajero(indice), "millas")
            elif opcion == 2:
                millasAacumular = int(input("Ingrese cantidad de millas para acumular: "))
                lista.acumularMillas(indice, millasAacumular)
                print(lista.getMillasdeViajero(indice), "millas")
            elif opcion == 3:
                millasAcanjear = int(input("Ingrese cantidad de millas a canjear: "))
                lista.canjearMillas(indice, millasAcanjear)
                print(lista.getMillasdeViajero(indice), "millas")
            else:
                print("Opción ingresada no corresponde")
            opcion = int(input("MENU:\nOpción 1: Consultar cantidad de Millas\nOpción 2: Acumular Millas\nOpcion 3: Canjear Millas\nOpcion 4: Salir\nEligir opción: "))
    else:
        print("Número de viajero no corresponde")
