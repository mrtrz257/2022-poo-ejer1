import csv

from PlanAhorro import PlanAhorro

class Manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def agregarPlan(self, plan):        #Agrega un objeto a la lista
        self.__lista.append(plan)
    def testPlanes(self):       #Abre el archivo csv y crea instancias de la clase PlanAhorro
        archivo = open("planes.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            codigoDePlan = fila[0]
            modeloDeVehiculo = fila[1]
            versionDeVehiculo = fila[2]
            precio = fila[3]
            unPlan = PlanAhorro(codigoDePlan, modeloDeVehiculo, versionDeVehiculo, precio)
            PlanAhorro.modCantidadCuotas(fila[4])
            PlanAhorro.modCuotasPagas(fila[5])
            self.agregarPlan(unPlan)
    def mostrarLista(self):
        for elemento in self.__lista:
            print('Codigo de Plan: {} - {:7} {:14} - Valor: {}'.format(elemento.getCodigoPlan(), elemento.getModeloVehiculo(), elemento.getVersionVehiculo(), elemento.getValorVehiculo()))
    def mostrarCuotas(self):
        for elemento in self.__lista:
            print('Cuotas a pagar para licitar: {}'.format(elemento.getCuotasPagas()))
    def ActualizarValorVehiculo(self):  #Modifica el valor de todos los vehiculos
        for elemento in self.__lista:
            print('Codigo de Plan: {} - Modelo de Vehiculo: {} - Version de Vehiculo: {}'.format(elemento.getCodigoPlan(), elemento.getModeloVehiculo(), elemento.getVersionVehiculo()))
            nuevoValor = int(input("Ingresar Nuevo Valor del Vehiculo: "))  #Ingresa nuevo valor
            elemento.modificarValor(nuevoValor)
    def ValorInferiorCuota(self, valor):  #Muestra los planes que tengan un valor de cuota menor a un valor ingresado
        for elemento in self.__lista:
            cuotas = elemento.getCantidadCuotas()
            if elemento.valorDeCuota(cuotas) < valor:   #Calcula el valor y lo compara
                print('Codigo de Plan: {} - {:7} {:14} - Tiene Valor de Cuota menor a {}'.format(elemento.getCodigoPlan(), elemento.getModeloVehiculo(), elemento.getVersionVehiculo(), valor))
    def montoLicitarVehiculo(self): #Muestra el monto a pagar para licitar los vehiculos
        for elemento in self.__lista:
            cuotas = elemento.getCuotasPagas()
            importeCuota = elemento.valorDeCuota(cuotas)
            monto = cuotas*importeCuota     #Calcula el monto
            print('Codigo de Plan: {} - {:7} {:14} - Monto a pagar para licitar el vehiculo: {}'.format(elemento.getCodigoPlan(), elemento.getModeloVehiculo(), elemento.getVersionVehiculo(), monto))
    def modificarCuotasAPagar(self): #Actualiza la cantidad de cuotas a pagar
        actCuotas = int(input("Ingresar cantidad de cuotas que deben estar pagas para licitar: "))
        for elemento in self.__lista:
            elemento.modCuotasPagas(actCuotas)
