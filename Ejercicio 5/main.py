from ManejadorPlanes import Manejador
from PlanAhorro import PlanAhorro

def test():
    print("TEST:")      #Crea un objeto de la clase PlanAhorro y la muestra para verificar que se creo correctamente
    test1 = PlanAhorro(320, "Ranger", "XLT", 7200000,)
    print(test1)
    print('Cuotas: {} - Cantidad de cuotas para licitar: {}'.format(test1.getCantidadCuotas(), test1.getCuotasPagas()))


if __name__=='__main__':
    test()
    lista = Manejador()
    lista.testPlanes()
    opcion = int(input("/-------------------/MENU/-------------------/\nOpción 1: Actualizar el Valor del Vehiculo de cada plan\nOpción 2: Mostrar Información segun valor de cuota\nOpción 3: Mostrar Monto para Licitar Vehiculos\nOpcion 4: Modificar cantidad de Cuotas Pagas para Licitar\nOpción 5: Salir\nEligir opción: "))
    while opcion != 5:
        if opcion == 1:     #Modificar el valor de todos los vehiculos
            lista.ActualizarValorVehiculo()
            lista.mostrarLista()
        elif opcion == 2:   #Compara el valor las cuotas con un valor ingresado por teclado
            cuotaComparacion = int(input("Ingresar Valor de Cuota para comparar: "))
            lista.ValorInferiorCuota(cuotaComparacion)
        elif opcion == 3:   #Muestra el monto a pagar para licitar los vehiculos
            lista.montoLicitarVehiculo()
        elif opcion == 4:    #Modifica las cantidad de cuotas a pagar para licitar
            #codigo = int(input("Ingresar codigo de plan: "))
            lista.modificarCuotasAPagar()
            print("Cantidad de cuotas se actualizo")
        else:
            print("Opción Ingresada no corresponde")
        opcion = int(input("/-------------------/MENU/-------------------/\nOpción 1: Actualizar el Valor del Vehiculo de cada plan\nOpción 2: Mostrar Información segun valor de cuota\nOpción 3: Mostrar Monto para Licitar Vehiculos\nOpcion 4: Modificar cantidad de Cuotas Pagas para Licitar\nOpción 5: Salir\nEligir opción: "))
    
