class Nodo:  # Agregar nodos sin .siguiente
    def __init__(self, value,siguiente=None):# value es obligatorio y siguiente opcional, si no se manda algo se pone None.
        self.data = value #falta encapsulamiento--> get and set
        self.siguiente = siguiente

class LinkedList:
    def __init__(self):#solo apunta head a la variable None.
        self.__head= None

class NodoDouble:
    def __init__(self,value,anterior = None,siguiente = None):
        self.data=value
        self.next=siguiente
        self.prev=anterior

class LinkedDoubleList:
    def __init__(self):#Metodo Constructor
        self.__head = None
        self.__tail = None #
        self.__size=0

    def get_size(self):#Regresa el numero total de nodos
        return self.__size

    def is_empty(self):#Regresa true si esta vacia, false si no.
        return self.__head == None

    def append(self,value): #Agrega el nodo al final entrando por Head.
        if self.is_empty():
            new = NodoDouble(value)
            self.__head=self.__tail=new
        else:
            new = NodoDouble(value,self.__tail,None)#valor,antes,siguiente
            self.__tail.next=new
            self.__tail=new
        self.__size += 1#incrementando el tamaño. para el get_size

    def transversal(self):#hacer el recorrido desde el head-tail
        curr_node=self.__head
        while curr_node != None:
            print(f"<--{curr_node.data}-->",end="")
            curr_node=curr_node.next
        print("")

    def reverse_transversal(self):#hacer el recorrido desde el tail-head
        curr_node=self.__tail
        while curr_node != None:
            print(f"<--{curr_node.data}-->",end="")
            curr_node=curr_node.prev
        print("")

    def remove_from_head(self,value):#remover desde Head-Tail
        curr_node=self.__head

        if self.__head.data == value:#si head es igual a value
            self.__head = self.__head.next
            self.__head.prev = None

        while curr_node.data != value and curr_node != None:
            curr_node=curr_node.next
        if curr_node.data == value:# 10<->20<->30
        #curr_node.prev es 10, curr_node.next es 30
        #curr_node.prev(osea 10).next(su siguiente)= curr_node.next(es 30)
            curr_node.prev.next=curr_node.next#
            curr_node.next.prev=curr_node.prev
        #Cuando next y prev ya no apunta a nada, elimina las conexciones.
        curr_node.next =None
        curr_node.prev =None
        self.__size -= 1
