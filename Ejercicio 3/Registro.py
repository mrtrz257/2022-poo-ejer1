
class Registro:
    __temperatura = 0
    __humedad = 0
    __presionAtmosferica = 0
    def __init__(self, temperatura = 0, humedad = 0, presionAtmosferica = 0):
        self.__temperatura = int(temperatura)
        self.__humedad = int(humedad)
        self.__presionAtmosferica = int(presionAtmosferica)
    def __str__(self):
        return '{:>13} {:>12} {:>12}'.format(self.__temperatura, self.__humedad, self.__presionAtmosferica)
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presionAtmosferica
    def Parametros(self):
        return [self.__temperatura, self.__humedad, self.__presionAtmosferica]
