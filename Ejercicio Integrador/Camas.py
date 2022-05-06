class Camas:
    __idCama = 0
    __Habitacion = 0
    __estado = True
    __apellidoNombre = ''
    __diagnostico = ''
    __fechaInternacion = ''
    __fechaAlta = ''
    def __init__(self, cama, habitacion, estado, nom, diagn, internacion, alta):
        self.__idCama = int(cama)
        self.__Habitacion = int(habitacion)
        self.__estado = bool(estado)
        self.__apellidoNombre = str(nom)
        self.__diagnostico = str(diagn)
        self.__fechaInternacion = str(internacion)
        self.__fechaAlta = str(alta)
    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.__idCama, self.__Habitacion, self.__estado, self.__estado, self.__apellidoNombre, self.__diagnostico, self.__fechaInternacion, self.__fechaAlta)
    def getIDCama(self):
        return self.__idCama
    def getHabitacion(self):
        return self.__Habitacion
    def getEstado(self):
        return self.__estado
    def getApellido(self):
        return self.__apellidoNombre
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaInt(self):
        return self.__fechaInternacion
    def getFechaAlta(self):
        return self.__fechaAlta
