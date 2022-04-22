import csv

from Email import Email

class ManejadorEmail:
    __listaEmails = None
    def __init__(self):
        self.__listaEmails = []
    def agregarMail(self, unMail):
        self.__listaEmails.append(unMail)
    def testMails(self):
        archivo = open("direcmails.csv")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if (band == True):
                band = False
            else:
                primerSplit = fila[0].split("@")
                segundoSplit = primerSplit[1].split(".")
                unMail = Email(primerSplit[0], segundoSplit[0], segundoSplit[1])
                self.agregarMail(unMail)
        archivo.close()
    def mostrarLista(self):
        for elemento in self.__listaEmails:
            print(elemento.retornaMail())
    def buscarIdentificador(self, identificador):
        contador = 0
        for i in self.__listaEmails:
            if(identificador == i.getIdCuenta()):
                contador += 1
        return contador
