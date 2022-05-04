from Conjunto import Conjunto

if __name__=='__main__':
    conjunto1 = Conjunto([1,2,3,4])
    conjunto2 = Conjunto([3,6])
    conjunto3 = Conjunto([3,7,9])
    conjunto4 = Conjunto([6,3])
    print('Conjunto 1: {}'.format(conjunto1))
    print('Conjunto 2: {}'.format(conjunto2))
    print('Conjunto 3: {}'.format(conjunto3))
    print('Conjunto 4: {}'.format(conjunto4))
    suma = conjunto1 + conjunto2
    print('Suma de Conjunto 1 y Conjunto 2: {}'.format(suma))
    resta = conjunto3 - conjunto4
    print('Resta de Conjunto 3 y Conjunto 4: {}'.format(resta))
    comparacion1 = conjunto2 == conjunto4
    comparacion2 = conjunto1 == conjunto3
    if comparacion1 == True:
        print("Conjunto 2 y Conjunto 4 son iguales")
    else:
        print("Conjunto 2 y Conjunto 4  NO son iguales")
    if comparacion2 == True:
        print("Conjunto 1 y Conjunto 3 son iguales")
    else:
        print("Conjunto 1 y Conjunto 3  NO son iguales")
