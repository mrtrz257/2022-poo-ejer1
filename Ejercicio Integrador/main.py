from ManejadorMedicamentos import ManejadorMedicamentos
from ManejadorCamas import ManejadorCamas
from Camas import Camas
from Medicamentos import Medicamentos

def test():
    test1 = Camas(4, 108, False, "Garcia, Nicolas", "Neumonia", "10/1/2022", "20/1/2022")
    test2 = Medicamentos(4, 4, "Motrin IB", "Ibuprofeno", "pastilla 2mg", 5, 1250)
    print('{} - {} - {} - {} - {} - {} - {}'.format(test1.getApellido(), test1.getIDCama(), test1.getHabitacion(),test1.getEstado(), test1.getDiagnostico(), test1.getFechaInt(), test1.getFechaAlta()))
    print('{} - {} - {} - {} - {} - {} - {}'.format(test2.getIDCama(), test2.getIdMed(), test2.getNombre(), test2.getMonodroga(), test2.getPresentacion(), test2.getCantidad(), test2.getPrecio()))

if __name__ == '__main__':
    test()
    lista = ManejadorMedicamentos()
    lista.crearLista()
    arreglo = ManejadorCamas()
    arreglo.crearArreglo()
    print("/-----------------------MENU-----------------------/")
    opcion = int(input("Opción 1: Mostrar Datos según Nombre de Paciente\nOpción 2: Mostrar Datos según Diagnostico\nOpción 3: Salir\nIngresar Opción: "))
    while opcion != 3:
        if opcion == 1: #Muestra Datos de un paciente segun nombre ingresado por teclado
            nombrePaciente = input("Ingrese 'Apellido, Nombre' de paciente: ")
            idPac = arreglo.buscarPaciente(nombrePaciente)
            if idPac != 0:
                print('{}'.format(arreglo.mostrarPaciente(idPac)))
                print("Medicamento/monodroga - Presentación - Cantidad - Precio: ")
                print('{}'.format(lista.datosMed(idPac)))
                print('Total Adeudado:                             ${}'.format(lista.totalAdeudado(idPac)))
            else: print("No se encontro paciente")
        elif opcion == 2:   #Muestra Datos de un paciente segun diagnostico ingresado por teclado
            BuscarDiagn = str(input("Ingresar Diagnostico: "))
            Diagn = arreglo.buscarDiagnostico(BuscarDiagn)
            if (len(Diagn) != 0):
                print(Diagn)
            else:
                print("No se encontro Diagnostico")
        else:
            print("Opción Ingresada No Corresponde")
        print("/-----------------------MENU-----------------------/")
        opcion = int(input(
            "Opción 1: Mostrar Datos según Nombre de Paciente\nOpción 2: Mostrar Datos según Diagnostico\nOpción 3: Salir\nIngresar Opción: "))
