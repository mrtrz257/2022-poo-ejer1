from Registro import Registro
import csv

class Manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def cantidadDias(self):     #Obtiene la cantidad de dias que tiene el archivo
        archivo = open("variablesMeteorologicas.csv")
        reader = csv.reader(archivo, delimiter=';')
        d = 0
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                if fila[1] == '23':
                    d += 1
        archivo.close()
        return d
    def crearLista(self, d):        #Crea la lista bidimensional y almacena los datos en ella
        self.__lista = [[]for i in range(d)]
        archivo = open("variablesMeteorologicas.csv")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        h = 23
        dia = 0
        for fila in reader:
            if band == True:
                band = False
            else:
                if h != 0:
                    unRegistro = Registro(fila[2], fila[3], fila[4])
                    self.__lista[dia].append(unRegistro)
                    h -= 1
                else:
                    unRegistro = Registro(fila[2], fila[3], fila[4])
                    self.__lista[dia].append(unRegistro)
                    dia += 1
                    h = 23
        archivo.close()
    def maximo(self, i):        #Calcula el maximo valor para cada variable, segun el indice
        d = 1
        h = 0
        max = -100
        diaMax = 0
        horaMax = 0
        for dia in self.__lista:
            for hora in dia:
                lista = hora.Parametros()
                if lista[i] > max:
                    max = lista[i]
                    diaMax = d
                    horaMax = h
                h += 1
            h = 0
            d += 1
        return [diaMax, horaMax, max]
    def minimo(self, i):        #Calcula el minimo valor para cada variable, segun el indice
        d = 1
        h = 0
        min = 10000
        diaMin = 0
        horaMin = 0
        for dia in self.__lista:
            for hora in dia:
                lista = hora.Parametros()
                if lista[i] < min:
                    min = lista[i]
                    diaMin = d
                    horaMin = h
                h += 1
            h = 0
            d += 1
        return [diaMin, horaMin, min]
    def promedio(self):         #Calcula la temperatura promedio para cada hora
        acum = [0]*24
        cont = [0]*24
        temp = []
        i = 0
        for dia in self.__lista:
            for hora in dia:
                acum[i] += int(hora.getTemperatura())
                cont[i] += 1
                i += 1
            i = 0
        for i in range(24):
            prom = acum[i] / cont[i]
            temp.append(prom)
        return temp
    def ListarDia(self, dia):       #Lista todas las variables segun numero de dia ingresado
        return self.__lista[dia-1]
