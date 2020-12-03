from array2d import Array2D
from stack import Stack

class LaberintoADT:
    #creamos el constructor.
    """
0 pasillos,1 pared,S salida, E entrada
pasillos es una tupla((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
entra en una tupla (5,2)
salida en una tupla (2,5)
    """
    def __init__(self,rens,cols,pasillos,entrada,salida):
        self.__laberinto=Array2D(rens,cols,'1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1] ,'0')#tomamos (2,1) 2 seria posicion 0 y 1 posicion 1
        self.set_entrada(entrada[0],entrada[1]) #mandamos a llamar salida y entrada.
        self.set_salida(salida[0],salida[1])
        self.__camino = Stack()
        self.__previa = None

#Pinta el laberinto
    def to_string(self):
        self.__laberinto.to_string()

#Establece la entrada "E" en la matriz, verificar limites perifericos.
    def set_entrada(self,ren,col):
        #Terminar la validacion de las coordenadas que cheque que este dentro de pasillos
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1] ,'0')
        self.__laberinto.set_item(ren,col,'E')

#Establece la salida "S" en la matriz, dentro de los limites perifericos de la matriz.
    def set_salida(self,ren,col):
        #Terminar la validacion de las coordenadas
        self.__laberinto.set_item(ren,col,'S')

#pregunta si nuestra posicion es igual a S=salida.
    def es_salida(self,ren,col):#antes de cambiar de lugar
        return self.__laberinto.set_item(ren,col)== 'S'

    def buscar_entrada(self):#se ejecuta antes de empezar a resolver
        encontrado =False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon,columna)=='E':
                    self.__camino.push(tuple(renglon,columna))#lo metemos a la pila como primer posicion
                    encontrado=True
        return encontrado

#guarda la tupla anterior
    def set_previa(self,pos_previa):
        self.__previa=pos_previa

    def get_previa(self):
        return self.__previa

        def resolver_labaerinto(self):
            pass
            #Aplicar reglas
