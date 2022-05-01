class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = str(num_viajero)
        self.__dni = int(dni)
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__millas_acum = int(millas_acum)
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def __radd__(self, acumulacionMillas):
        self.__millas_acum = self.__millas_acum + acumulacionMillas
        return self.__millas_acum
    def __rsub__(self, millasACanjear):
        if millasACanjear <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - millasACanjear
            return self.__millas_acum
        else:
            print("Error en la operación")
    def __eq__(self, other):
        return  other == self.__millas_acum
    def getNumViajero(self):
        return self.__num_viajero
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def __gt__(self, other):
        return self.__millas_acum < other.cantidadTotaldeMillas()
