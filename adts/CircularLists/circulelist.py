class Nodo:
    def __init__(self, value, siguiente=None, anterior=None):
        self.data=value
        self.next=siguiente
        self.prev=anterior
class CiruleLists:
    def __init__(self):
        self.__head=None
        self.__tail=Nonde
        self.__size=0

    def get_size(self):# Regresa el numero de elemntos.
        return self.__size

    def is_empty(self):#pregunta lista vacia?
        return self.__head==None

    
