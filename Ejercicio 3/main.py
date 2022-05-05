from ManejadorRegistro import Manejador
from Registro import Registro

def test():
    test1 = Registro(35, 47, 1008)       #Crea una instancia de la clase Registro y la muestra para verificar que se creo correctamente
    print('TEST: Temperatura: {}° - Humedad: {}% - Presion Atmosferica {} hPa'.format(test.getTemperatura(), test.getHumedad(), test.getPresion()))

if __name__ =='__main__':
    test()
    lista = Manejador()
    dias = lista.cantidadDias()
    lista.crearLista(dias)
    print('/====================MENU====================/')
    opcion = int(input("Opción 1: Indicar Valores Maximos y Minimos de Variables con Día y Hora\nOpción 2: Listar Temperatura Promedio Mensual por cada hora\nOpción 3: Listar Valores para cada Hora para un Día dado\nOpcion 4: Salir\nIngresar Opción: "))
    while opcion != 4:
        if opcion == 1:
            print('/--------------------/Valores Maximos/--------------------/')
            Max = lista.maximo(0)
            print('Dia: {} - Hora: {} Hrs - Temperatura Maxima: {}°'.format(Max[0], Max[1], Max[2]))
            Max = lista.maximo(1)
            print('Dia: {} - Hora: {} Hrs - Humedad Maxima: {}%'.format(Max[0], Max[1], Max[2]))
            Max = lista.maximo(2)
            print('Dia: {} - Hora: {} Hrs - Presión Atmosferica Maxima: {} hPa'.format(Max[0], Max[1], Max[2]))
            print('/--------------------/Valores Minimos/--------------------/')
            Min = lista.minimo(0)
            print('Dia: {} - Hora: {} Hrs - Temperatura Minima: {}°'.format(Min[0], Min[1], Min[2]))
            Min = lista.minimo(1)
            print('Dia: {} - Hora: {} Hrs - Humedad Minima: {}%'.format(Min[0], Min[1], Min[2]))
            Min = lista.minimo(2)
            print('Dia: {} - Hora: {} Hrs - Presión Atmosferica Minima: {} hPa'.format(Min[0], Min[1], Min[2]))
        elif opcion == 2:
            pr = lista.promedio()
            hora = 0
            print("Promedio de Temperatura por cada Hora:")
            for elemento in pr:
                print('A la Hora {}, Temperatura Promedio: {}°'.format(hora, elemento))
                hora += 1
        elif opcion == 3:
            dia = int(input("Ingresar dia para mostrar Variables: "))
            h = 0
            print("Hora    Temperatura    Humedad    Presión")
            for elemento in lista.ListarDia(dia):
                print('{} {}'.format(h, elemento))
                h += 1
        else:
            print("Opción No Corresponde")
        print('/====================MENU====================/')
        opcion = int(input("Opción 1: Indicar Valores Maximos y Minimos de Variables con Día y Hora\nOpción 2: Listar Temperatura Promedio Mensual por cada hora\nOpción 3: Listar Valores para cada Hora para un Día dado\nOpcion 4: Salir\nIngresar Opción: "))
