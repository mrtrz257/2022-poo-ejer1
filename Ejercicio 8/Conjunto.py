class Conjunto:
    __conjunto_num = []
    def __init__(self, conjunto = []):
        self.__conjunto_num = conjunto
    def __str__(self):
        return '{}'.format(self.__conjunto_num)
    def getConjunto(self):
        return self.__conjunto_num
    def __add__(self, other):   #Sobrecarga de operador +
        listaSum = self.__conjunto_num
        for elemento in other.getConjunto():
            if elemento not in listaSum:
                listaSum.append(elemento)
        return Conjunto(listaSum)
    def __sub__(self, other):   #Sobrecarga de operador -
        listaRes = self.__conjunto_num
        for elemento in other.getConjunto():
            if elemento in listaRes:
                listaRes.remove(elemento)
        return Conjunto(listaRes)
    def __eq__(self, other):    #Sobrecarga de operador =
        i = 0
        band = True
        listaEq = other.getConjunto()
        listaEq.sort()
        if(len(listaEq))==len(self.__conjunto_num):
            listaEq = other.getConjunto
            while band == False:
                i += 1
                if self.__conjunto_num[i] != listaEq[i]:
                    band = False
        else:
            band = False
        return band
