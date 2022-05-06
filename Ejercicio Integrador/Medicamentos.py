class Medicamentos:
    __idCama = 0
    __idMedicamento = ''
    __nombreComercial = ''
    __monodroga = ''
    __presentacion = ''
    __cantidadAplicada = 0
    __precioTotal = 0
    def __init__(self, IDCama, IDMed, nombre, monodroga, presentacion, cantidad, precio):
        self.__idCama = int(IDCama)
        self.__idMedicamento = str(IDMed)
        self.__nombreComercial = str(nombre)
        self.__monodroga = str(monodroga)
        self.__presentacion = str(presentacion)
        self.__cantidadAplicada = int(cantidad)
        self.__precioTotal = int(precio)
    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.__idCama, self.__idMedicamento, self.__nombreComercial, self.__monodroga, self.__presentacion, self.__cantidadAplicada, self.__precioTotal)
    def getIDCama(self):
        return self.__idCama
    def getIdMed(self):
        return self.__idMedicamento
    def getNombre(self):
        return self.__nombreComercial
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidad(self):
        return self.__cantidadAplicada
    def getPrecio(self):
        return self.__precioTotal
