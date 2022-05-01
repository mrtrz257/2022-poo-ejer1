import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:
    __listaViajeros = None
    def __init__(self):
        self.__listaViajeros = []
    def agregarViajero(self, unViajero):
        self.__listaViajeros.append(unViajero)
    def testViajeros(self):
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
            print('ID: {} - {} {:10} - Millas: {}'.format(elemento.getNumViajero(), elemento.getNombre(), elemento.getApellido(), elemento.cantidadTotaldeMillas()))
    def buscarViajero(self, numViajero):
        for indice, viajero in enumerate(self.__listaViajeros):
            if viajero.getNumViajero() == numViajero:
                return indice
    def getMillasdeViajero(self, numViajero):
        return self.__listaViajeros[numViajero].cantidadTotaldeMillas()
    def acumularMillas(self, numViajero, millas):
        return millas + self.__listaViajeros[numViajero]
    def canjearMillas(self, numViajero, millas):
        return millas - self.__listaViajeros[numViajero]
    def ordenarLista(self):
        self.__listaViajeros.sort()
    def compararMillas(self, millas):
        cont = 0
        for elemento in self.__listaViajeros:
            if elemento.cantidadTotaldeMillas() == millas:
                print('{} {} tiene {} millas'.format(elemento.getNombre(),elemento.getApellido(), elemento.cantidadTotaldeMillas()))
            else:
                cont += 1
        return cont
