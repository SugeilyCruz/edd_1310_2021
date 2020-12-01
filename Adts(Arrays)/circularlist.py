class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value
        self.next=siguiente

class CircularLists:#à Constructor
    def __init__(self):
        self.__head=None
        self.__ref=None #Self.__tail==> el mayor.
        self.__size=0

    def get_ref(self):
        if self.is_empty():
            print("Lista vacia")
        else:
            print("Head==>", self.__head.data)
            print("Ref==>", self.__ref.data)
            print("Ref.siguiente que apunta a Head==>", self.__ref.siguiente.data)

    def get_size(self):# Regresa el numero de elemntos.
        return print(f"Size==>{self.__size}")

    def is_empty(self):#à esta vacía?
        return self.__head==None

    def insert(self,value=None):#Agrega el nodo de forma ordenada
        new=Nodo(value)
        if self.is_empty():
            self.__head=self.__ref=new
            self.__ref.siguiente=self.__head
            self.__size+=1
        elif value == None:
            pass
        elif self.search(value)== True:#Valor ya en lista
            print(f"El valor {value} ya se encuentra en la lista")
        elif value > self.__ref.data: #New > tail
            curr_ref=self.__ref
            self.__ref=curr_ref.siguiente=new
            self.__ref.siguiente=self.__head
            self.__size+=1
        else:
            if value < self.__head.data: #New < head
                new.siguiente=self.__head
                self.__head= new
                self.__ref.siguiente=self.__head
                self.__size+=1
            else:
                if value > self.__head.data:#New | menor | intermedios | mayor |
                    curr_ref=self.__ref.siguiente
                    while value > curr_ref.data:
                        curr_ant=curr_ref
                        curr_ref=curr_ref.siguiente
                    new.siguiente=curr_ant.siguiente
                    curr_ant.siguiente=new
                    self.__size+=1

    def search(self,value=None):#à busca el elemento value y regresa true o false.
        info=False
        if self.is_empty():
            print("Lista vacia")
        else:
            curr_ref=self.__ref #3 4 5 6
            while curr_ref.siguiente != self.__ref:
                if curr_ref.data==value:
                    info=True
                curr_ref=curr_ref.siguiente
            if curr_ref.data==value:
                info=True
            return info

    def remove(self,value=None):#elimina el elemento value.
        if self.is_empty():
            print("Lista vacia")
        elif value==None:
            pass
        elif self.__head==self.__ref:
            self.__head=self.__ref=None
            self.__size-=1
        else:
            curr_ref=self.__ref# 5 7 8 9 10
            while curr_ref.data != value and curr_ref.siguiente != self.__ref:
                curr_ant=curr_ref
                curr_ref=curr_ref.siguiente
            print(f"Nodo removido: {curr_ref.data}")
            if curr_ref.data == self.__head.data:
                self.__head = self.__head.siguiente
                self.__ref.siguiente=self.__head
                self.__size-=1
            elif curr_ref.data == self.__ref.data:
                curr_ref2=self.__head
                while curr_ref2.siguiente != self.__ref:
                    curr_ref2=curr_ref2.siguiente
                curr_ref2.siguiente=self.__head
                self.__ref= curr_ref2
                self.__size-=1
            else:
                curr_ant.siguiente=curr_ant.siguiente.siguiente
                self.__size-=1

    def transversal(self):#Recorrido transversal
        if self.is_empty():
            print("Lista vacia")
        else:
            curr_node=self.__ref
            while curr_node.siguiente != self.__ref:
                print(f"{curr_node.siguiente.data}==>",end="")
                curr_node= curr_node.siguiente
            print(f"{curr_node.siguiente.data}==>")
