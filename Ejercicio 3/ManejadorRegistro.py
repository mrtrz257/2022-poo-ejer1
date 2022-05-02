from Registro import Registro
import csv

class Manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def testLista(self):
        archivo = open("variablesMeteorologicas.csv")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
