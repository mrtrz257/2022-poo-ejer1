from Email import Email
from ManejadorEmail import ManejadorEmail

if __name__=='__main__':
    nom = input("Ingrese Nombre: ")
    idcuent = input("Ingrese ID de Correo: ")
    dom = input("Ingrese Dominio de Correo: ")
    tipoDom = input("Ingrese Tipo de Dominio de Correo (ej: com, net): ")
    contr = input("Ingrese Contraseña: ")
    unMail = Email(idcuent, dom, tipoDom, contr)
    print("Estimado", nom, ", te enviaremos tus mensajes a la dirección", unMail.retornaMail())
    modifContr = input("Para modificar contraseña, ingrese contraseña actual: ")
    if modifContr==contr:
        contr = input("Ingrese nueva contraseña: ")
        unMail.modificaContrasena(contr)
    else: print("Contraseña ingresada no coincide")
    otroMail = Email()
    direcMail = input("Ingrese Email completo: ")
    otroMail.crearCuenta(direcMail)
    print(otroMail.retornaMail())
    lista = ManejadorEmail()
    lista.testMails()
    lista.mostrarLista()
    idDeCuenta = input("Ingrese identificador de cuenta a buscar: ")
    if (lista.buscarIdentificador(idDeCuenta) > 1):
        print("El identificador esta repetido")
    else: print("El identificador NO se repite o NO se encontro")
