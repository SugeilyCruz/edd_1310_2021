class Nodo:
    def __init__( self , dato ):
        self.__dato = dato
        self.__siguiente = None

    def get_dato( self ):
        return self.__dato

    def set_dato( self , d ):
        self.__dato = d

    def get_siguiente( self ):
        return self.__siguiente

    def set_siguiente( self , d ):
        self.__siguiente = d

def show(self):
    curr_node=self#Head #es el pibote que se va moviendo
    print("Inicio de la estructura ligada")
    print("|" + str(curr_node.get_dato())+ "| -->", end="")
    while(curr_node.get_siguiente() !=None):
      curr_node = curr_node.get_siguiente()
      print("|" + str(curr_node.get_dato()) + "| -->", end="")
    print("\nFin")
