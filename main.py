from Email import Email

if __name__=='__main__':
    print("Ingrese nombre, id de cuenta, dominio, tipo de dominio de email y contraseña")
    nom = input()
    idcuent = input()
    dom = input()
    tipoDom = input()
    contr = input()
    unMail = Email(idcuent, dom, tipoDom, contr)
    print("Estimado", nom, ", te enviaremos tus mensajes a la dirección", unMail.retornaMail())
    print("Para modificar contraseña, ingrese contraseña actual")
    modifContr = input()
    if modifContr==contr:
        print("Ingrese nueva contraseña:")
        contr = input()
        unMail.modificaContrasena(contr)
    else: print("Contraseña ingresada no coincide")
    print("Ingrese Email completo: ")
    direcMail = input()
