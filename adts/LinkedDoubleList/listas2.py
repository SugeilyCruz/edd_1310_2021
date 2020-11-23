class NodoDouble:
    def __init__(self,value,despues = None,antes = None):
        self.data=value
        self.next=despues
        self.prev=antes

class LinkedDoubleList:
    def __init__(self):#Metodo Constructor
        self.__head= None
        self.__tail= None
        self.__size=0

    def get_size(self):# Regresa el numero de elemntos.
        curr_node=self.__head
        while curr_node != None:
            curr_node= curr_node.next
            self.__size += 1
        return self.__size

    def is_empty(self):#Regresa true si esta vacia, false si no.
        return self.__head == None

    def append(self,value): #Agrega el nodo al final entrando por Head.
        new = NodoDouble(value)
        curr_node=self.__head
        if self.is_empty():
            self.__head=self.__tail=new
        else:
            while curr_node.next != None:
                curr_node= curr_node.next
            curr_new=self.__tail
            self.__tail=curr_node.next=new
            self.__tail.prev=curr_new

    def transversal(self): #Recorrido desde Head.
        curr_node=self.__head
        while curr_node != None:
            print(f"{curr_node.data}<==>",end="")
            curr_node=curr_node.next
        print("")

    def reverse_transversal(self): #Recorrido desde Tail.
        curr_node=self.__tail
        while curr_node != None:
            print(f"{curr_node.data}<==>",end="")
            curr_node=curr_node.prev
        print("")

    def find_from_head(self,value=None): #A buscar a partir de head
        index=1
        dato= "El dato no esta dentro de la lista"
        posicion=None
        curr_node=self.__head
        if curr_node==value:
            dato = value
            posicion= index
        else:
            while curr_node != None:
                if curr_node.data == value:
                    posicion= index
                    dato=curr_node.data
                index+=1
                curr_node=curr_node.next
        return print(f"Dato: {dato} en posicion: {posicion} de Head-Tail ")

    def find_from_tail(self,value=None):
        index=1
        dato= "El dato no esta dentro de la lista"
        posicion= None
        curr_node=self.__tail
        if curr_node == value:
            dato = value
            posicion= index
        else:
            while curr_node !=None:
                if curr_node.data == value:
                    posicion= index
                    dato= curr_node.data
                index+=1
                curr_node=curr_node.prev
        return print(f"Dato: {dato} en posicion: {posicion} de Tail-Head ")

    def remove_from_head(self,value): #Eliminar a partir de head
        curr_node=self.__head
        while curr_node.data != value and curr_node.next != None:
            curr_new=curr_node
            curr_node= curr_node.next

        if curr_node.data == value and curr_node.data != self.__head.data:
            curr_new.next= curr_new.next.next
            (curr_new.next).prev = curr_node.prev
        else:
            if curr_node.data == self.__head.data:
                self.__head = curr_node.next
                self.__head.prev = None

            elif self.__tail.data == value:
                self.__tail.prev.next = None
                self.__tail = self.__tail.prev #TailNuevo

    def remove_from_tail(self,value): #Eliminar a partir de Tail
        curr_node=self.__tail
        while curr_node.data != value and curr_node.prev != None:
            curr_new=curr_node
            curr_node= curr_node.prev

        if curr_node.data == value and curr_node.data != self.__tail.data:
            curr_new.prev= curr_new.prev.prev
            (curr_new.prev).next = curr_node.next
        else:
            if curr_node.data == self.__tail.data:
                self.__tail = curr_node.prev
                self.__tail.next = None

            elif self.__head.data == value:
                self.__head.next.prev = None
                self.__head = self.__head.next #HeadNuevo

""" i = self.__size - 1 - index
        cont = 0
        curr_nodeTail = self.__tail
        curr_nodeTail_ant = self.__tail
        while(curr_nodeTail):
            if cont == i :
                if cont == 0:
                    curr_op=curr_nodeTail_ant.prev
                    curr_nodeTail_ant.next=curr_op
                else:
                    curr_nodeTail_ant = curr_nodeTail.next
                    curr_nodeTail_ant.prev = curr_nodeTail_ant.prev.prev
            cont += 1
            curr_nodeTail = curr_nodeTail.prev """
"""
● DoubleLinkedList( ) à Constructor
● get_size à regresa el número de elementos.
● is_empty() --> esta vacía?
● append( value) --> Agrega el nodo al final entrando por head.
● find_from_tail( value ) à buscar a partir de tail regresar la posicion
● find_from_head( value ) à buscar a partir de head
● remove_from_tail( value ) à eleiminar a partir de tail
● remove_from_head( value ) à eliminar a partir de head
● transversal() à recorrido desde head
● reverse_transversal à recorrido desde el final

"""
