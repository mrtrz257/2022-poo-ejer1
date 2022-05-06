import csv
from Medicamentos import Medicamentos

class ManejadorMedicamentos:
    __lista = []
    def __init__(self):
        self.__lista = []
    def agregarMedicamento(self, unMed):
        self.__lista.append(unMed)
    def crearLista(self):   #Abre el archivo, crea la lista y agrega instancias de la clase Medicamentos
        archivo = open("medicamentos.csv")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                unMed = Medicamentos(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.agregarMedicamento(unMed)
        archivo.close()
    def mostrarLista(self): #Muestra la id y el nombre de todos los medicamentos
        texto = ''
        for elemento in self.__lista:
            texto += '{} {}'.format(elemento.getIdMed(), elemento.getNombre()) + '\n'
        return texto
    def datosMed(self, id):    #Muestra los datos de los medicamentos segun la id del paciente
        text = ''
        for elemento in self.__lista:
            if elemento.getIDCama() == id:
                text += '{}/{} - {} - {} - ${}'.format(elemento.getNombre(), elemento.getMonodroga(), elemento.getPresentacion(), elemento.getCantidad(), elemento.getPrecio()) + '\n'
        return text
    def totalAdeudado(self, id):    #Calcula el total adeudado de los medicamentos
        tot = 0.0
        for elemento in self.__lista:
            if elemento.getIDCama() == id:
                tot += elemento.getPrecio()
        return tot
