
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''
    def __init__(self, idCuenta = '', dominio = '', tipoDominio = '', contrasena = ''):
        self.__idCuenta = str(idCuenta)
        self.__dominio = str(dominio)
        self.__tipoDominio = str(tipoDominio)
        self.__contrasena = str(contrasena)
    def retornaMail(self):
        return ('{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio))
    def getDominio(self):
        return self.__dominio
    def getIdCuenta(self):
        return self.__idCuenta
    def modificaContrasena(self, contrasena):
        self.__contrasena = contrasena
    def crearCuenta(self, direccionMail):
        primerSplit = direccionMail.split("@", 1)
        segundoSplit = primerSplit[1].split(".", 1)
        self.__idCuenta = primerSplit[0]
        self.__dominio = segundoSplit[0]
        self.__tipoDominio = segundoSplit[1]
