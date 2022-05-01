from ManejadorPlanes import Manejador

if __name__=='__main__':
    lista = Manejador()
    lista.testPlanes()
    opcion = int(input("/-------------------/MENU/-------------------/\nOpción 1: Actualizar el Valor del Vehiculo de cada plan\nOpción 2: Mostrar Información segun valor de cuota\nOpción 3: Mostrar Monto para Licitar Vehiculos\nOpcion 4: Modificar cantidad de Cuotas Pagas para Licitar\nOpción 5: Salir\nEligir opción: "))
    while opcion != 5:
        if opcion == 1:
            lista.ActualizarValorVehiculo()
            lista.mostrarLista()
        elif opcion == 2:
            cuotaComparacion = int(input("Ingresar Valor de Cuota para comparar: "))
            lista.ValorInferiorCuota(cuotaComparacion)
        elif opcion == 3:
            lista.montoLicitarVehiculo()
        elif opcion == 4:
            #codigo = int(input("Ingresar codigo de plan: "))
            lista.modificarCuotasAPagar()
            print("Cantidad de cuotas se actualizo")
        else:
            print("Opción Ingresada no corresponde")
        opcion = int(input("/-------------------/MENU/-------------------/\nOpción 1: Actualizar el Valor del Vehiculo de cada plan\nOpción 2: Mostrar Información segun valor de cuota\nOpción 3: Mostrar Monto para Licitar Vehiculos\nOpcion 4: Modificar cantidad de Cuotas Pagas para Licitar\nOpción 5: Salir\nEligir opción: "))
