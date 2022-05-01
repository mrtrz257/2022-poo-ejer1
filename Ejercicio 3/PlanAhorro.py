class PlanAhorro:
    cantidadCuotas = 0
    cutoasPagasParaLicitar = 0
    def __init__(self, codigoPlan = '',modeloVehiculo = '', versionVehiculo = '', valorVehiculo = ''):
        self.__codigoPlan = int(codigoPlan)
        self.__modeloVehiculo = str(modeloVehiculo)
        self.__versionVehiculo = str(versionVehiculo)
        self.__valorVehiculo = int(valorVehiculo)
    #Metodos de Instancia
    def getCodigoPlan(self):
        return int(self.__codigoPlan)
    def getModeloVehiculo(self):
        return self.__modeloVehiculo
    def getVersionVehiculo(self):
        return self.__versionVehiculo
    def getValorVehiculo(self):
        return self.__valorVehiculo
    def modificarValor(self, nuevoValor):
        self.__valorVehiculo = nuevoValor
    def valorDeCuota(self, cuotas):
        return (self.__valorVehiculo/ cuotas) + self.__valorVehiculo * 0.1
    #Metodos de Clase
    @classmethod
    def getCantidadCuotas(cls):
        return cls.cantidadCuotas
    @classmethod
    def getCuotasPagas(cls):
        return cls.cutoasPagasParaLicitar
    @classmethod
    def modCantidadCuotas(cls, cuotas):
        cls.cantidadCuotas = int(cuotas)
    @classmethod
    def modCuotasPagas(cls, cuotas):
        cls.cutoasPagasParaLicitar = int(cuotas)
