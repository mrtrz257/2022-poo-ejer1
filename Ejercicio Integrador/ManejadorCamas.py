import csv
from Camas import Camas
import numpy as np

class ManejadorCamas:
    __arreglo = None
    def __init__(self):
        self.__arreglo = None
    def __str__(self):
        return '{}'.format(self.__arreglo)
    def crearArreglo(self):     #Abre el archivo, crea el arreglo y se le agregan instancias de la clase Camas
        self.__arreglo = np.empty(3, dtype=Camas)
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        i = 0
        for fila in reader:
            if band == True:
                band = False
            else:
                unaCama = Camas(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.__arreglo[i] = unaCama
                i += 1
        archivo.close()
    def buscarPaciente(self, paciente): #Busca la id de un paciente segun el nombre ingresado
        id = 0
        for elemento in self.__arreglo:
            if paciente == elemento.getApellido():
                id = elemento.getIDCama()
        return id
    def mostrarPaciente(self, id):  #Muestra los datos de un paciente segun la id de Cama
        texto = ''
        for elemento in self.__arreglo:
            if id == elemento.getIDCama():
                texto += 'Paciente: {}      Cama: {}    Habitación: {} \nDiagnóstico: {}      Fecha de Internación: {} \nFecha de alta: {}'.format(elemento.getApellido(), elemento.getIDCama(), elemento.getHabitacion(), elemento.getDiagnostico(), elemento.getFechaInt(), elemento.getFechaAlta())
        return texto
    def buscarDiagnostico(self, diagn): #Muestra los datos de un paciente segun un diagnostico ingresado
        datos = ''
        for elemento in self.__arreglo:
            if elemento.getDiagnostico() == diagn:
                datos = 'Nombre: {} - Cama: {} - Habitación: {} - Fecha de Internación: {} - Fecha de Alta: {}'.format(elemento.getApellido(), elemento.getIDCama(), elemento.getHabitacion(), elemento.getFechaInt(), elemento.getFechaAlta())
        return datos
