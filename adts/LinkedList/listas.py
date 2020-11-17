class Nodo:  # Agregar nodos sin .siguiente
    def __init__(self, value,siguiente=None):# value es obligatorio y siguiente opcional, si no se manda algo se pone None.
        self.data = value #falta encapsulamiento--> get and set
        self.siguiente = siguiente
class LinkedList:
    def __init__(self):#solo apunta head a la variable None.
        self.__head= None

    def is_empty(self):
        return self.__head == None #pregunta si head esta apuntando a Nune=vacio o ya tiene un valor.

    def append(self,value):#agregar un nuevo nodo.
        nuevo= Nodo(value)# creo cuanto va a valer mi nuevo nodo con value.
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
            curr_node= curr_node.siguiente
        if curr_node.data == value:#curr == None tambien. me sali porque encontre el valor o porque es el final.
            #curr_node = tenemos que declarar un nuevo para que guarde el nodo anterior y que se conecta al siguiente. osea 5 al 20.
