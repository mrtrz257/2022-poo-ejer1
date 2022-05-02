
class Ventana:
    __Titulo = ''
    __x_SuperiorIzquierdo = 0
    __y_SuperiorIzquierdo = 0
    __x_InferiorDerecho = 500
    __y_InferiorDerecho = 500
    def __init__(self, Titulo = '', XsupIzq = 0, YsupIzq = 0, XinfDer = 500, YinfDer = 500):
        self.__Titulo = Titulo
        self.__x_SuperiorIzquierdo = XsupIzq
        self.__y_SuperiorIzquierdo = YsupIzq
        self.__x_InferiorDerecho = XinfDer
        self.__y_InferiorDerecho = YinfDer
    def getTitulo(self):
        return self.__Titulo
    def alto(self):
        return self.__x_InferiorDerecho - self.__x_SuperiorIzquierdo
    def ancho(self):
        return self.__y_InferiorDerecho - self.__y_SuperiorIzquierdo
    def mostrar(self):
        print('{}: Vertice Superior Izquierdo: {} {} - Vertice Inferior Derecho: {} {}'.format(self.__Titulo, self.__x_SuperiorIzquierdo, self.__y_SuperiorIzquierdo, self.__x_InferiorDerecho, self.__y_InferiorDerecho))
    def moverDerecha(self, x):
        self.__x_SuperiorIzquierdo += x
        self.__x_InferiorDerecho += x
    def moverIzquierda(self, x):
        self.__x_SuperiorIzquierdo -= x
        self.__x_InferiorDerecho -= x
    def bajar(self, y=0):
        self.__y_SuperiorIzquierdo -= y
        self.__y_InferiorDerecho -= y
    def subir(self, y=0):
        self.__y_SuperiorIzquierdo += y
        self.__y_InferiorDerecho += y
