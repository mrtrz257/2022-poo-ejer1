
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''
    def __init__(self, idCuenta = '', dominio = '', tipoDominio = '', contrasena = ''):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = contrasena
    def retornaMail(self):
        return ('{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio))
    def getDominio(self):
        return self.__dominio
    def modificaContrasena(self, contrasena):
        self.__contrasena = contrasena
    def crearCuenta(self, direccionMail):
        primerSplit = direccionMail.split("@")
        segundoSplit = primerSplit[1].split(".")
        otroCorreo = Email(primerSplit[0], segundoSplit[0], segundoSplit[1])
        
