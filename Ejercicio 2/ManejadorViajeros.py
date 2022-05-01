import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:
    __listaViajeros = None
    def __init__(self):
        self.__listaViajeros = []
    def agregarViajero(self, unViajero):
        self.__listaViajeros.append(unViajero)
    def testViajeros(self):             #Abre el archivo y crea instancias de la clase ViajeroFrecuente
        archivo = open("archivoViajeros.csv")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if (band == True):
                band = False
            else:
                numeroViajero = fila[0]
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = fila[4]
                unViajero = ViajeroFrecuente(numeroViajero, dni, nombre, apellido, millas)
                self.agregarViajero(unViajero)
        archivo.close()
    def mostrarLista(self):
        for elemento in self.__listaViajeros:
            print(elemento.cantidadTotaldeMillas())
    def buscarViajero(self, numViajero):
        for indice, viajero in enumerate(self.__listaViajeros):
            if viajero.getNumViajero() == numViajero:
                return indice
    def getMillasdeViajero(self, numViajero):
        return self.__listaViajeros[numViajero].cantidadTotaldeMillas()
    def acumularMillas(self, numViajero, millas):
        return self.__listaViajeros[numViajero].acumularMillas(millas)
    def canjearMillas(self, numViajero, millas):
        return self.__listaViajeros[numViajero].canjearMillas(millas)
