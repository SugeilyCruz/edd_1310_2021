class Nodo:  # Agregar nodos sin .siguiente
    def __init__(self, value,siguiente=None):# value es obligatorio y siguiente opcional, si no se manda algo se pone None.
        self.data = value #falta encapsulamiento--> get and set
        self.siguiente = siguiente
class LinkedList:
    def __init__(self):#solo apunta head a la variable None.
        self.__head= None

    def is_empty(self):
        return self.__head == None #pregunta si head esta apuntando a None=vacio o ya tiene un valor.

    def append(self,value):#agregar un nuevo nodo.
        nuevo= Nodo(value)#mi nuevo nodo con value.
        if self.__head == None: #self.is_empty() La lista esta vacia.
            self.__head=nuevo
        else:#la lista no esta vacia, ya tiene un valor en head
            curr_node = self.__head#igualo al primer valor
            while curr_node.siguiente != None:#mientrsa curr sea diferente de none
                curr_node = curr_node.siguiente # apunta a todo un nodo. le da el valor de .siguiente a curr para cuando entre otra vez.
            curr_node.siguiente= nuevo
    def transversal(self):#imprime todos mis nodos.
        curr_node=self.__head
        while curr_node != None:# cuando es diferente de none entra y agrega el siguiente a curr_node. cuando es none ya solo imprime un salto.
#una cosa es data que es el valor 10,5,6,etc y otra cosa es .siguiente si tiene valor o no(es el punto en el dibujo).
            print(f"{curr_node.data} -->", end="")#el end es para quitar el salto de linea.
            curr_node= curr_node.siguiente#agrega el nuevo nodo a curr_node, estamos formando una lista
        print("")#cuando curr es igual a none imprime un ""

    def remove(self,value):
        curr_node=self.__head
        while curr_node.data != value and curr_node.siguiente != None:#mientras que curr sea diferente del valor que pedimos y sea diferente de none(que no hayamos llegado al final.)
            curr_new=curr_node# guardamos el nodo antes de que pase al siguiente y lo guarde.
            curr_node= curr_node.siguiente
        if curr_node.data == value and curr_node.data != self.__head.data:
            curr_new.siguiente= curr_node.siguiente#el numero siguiente de 5 sera 20
        else:
            if curr_node.data == self.__head.data:
                self.__head = self.__head.siguiente

    def preppend(self,value): #Agrega el nuevo nodo al principio de head.
        nuevo=Nodo(value, self.__head)
        self.__head= nuevo

    def tail(self):#Regresa el ultimo nodo.
        curr_node=self.__head
        while curr_node.siguiente != None:
            curr_node= curr_node.siguiente
        return curr_node

    def get(self,posicion = None):#por defecto regresa el ultimo. #Terminar tarea
    contador=0
    dato=None
    if posicion == None:
        dato=self.tail().data
    else:
        pass
    return dato


#OPCIONALES 
    #Agregar antes de la primer coincidiencia, si no encuentra la referencia no hace la inserccion.
    def add_before(self,reference_value,value):
        nuevo= Nodo(value)
        curr_node=self.__head
        while curr_node.data != reference_value and curr_node.siguiente != None:#busca nuestro nodo de referencia.
            curr_new=curr_node
            curr_node= curr_node.siguiente
        if curr_node.data == reference_value and curr_node.data != self.__head.data:#nodo igual a referencia y diferente a head.
            curr_new.siguiente=nuevo
            curr_new.siguiente.siguiente=curr_node
        else:#si no es el caso entra aqui y pregunta nodo igual a head.
            if curr_node.data == reference_value:
                self.__head=nuevo
                nuevo.siguiente=curr_node
    #Agregar después de la referencia
    def add_after(self,reference_value,value):
        nuevo= Nodo(value)
        curr_node=self.__head
        while curr_node.data != reference_value and curr_node.siguiente != None:#busca nuestro nodo de referencia.
            curr_node= curr_node.siguiente
            curr_new= curr_node.siguiente#guarada el valor de curr_node(curr_node= curr_node.siguiente).
        if curr_node.data == reference_value and curr_node.data != self.__head.data:#nodo igual a referencia y diferente a head.
            curr_node.siguiente=nuevo
            curr_node.siguiente.siguiente=curr_new
        else:
            if curr_node.data == reference_value:
                curr_new = curr_node.siguiente
                curr_node.siguiente=nuevo
                curr_node.siguiente.siguiente=curr_new
