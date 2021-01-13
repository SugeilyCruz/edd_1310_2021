class Stack:
    def __init__(self):
        self.__data=list() #podria ser []
        #self.__size=0

    def is_empty(self):#Si la lista es igual a 0 es que esta vacia regresa true.
        return len(self.__data)==0

    def length(self):#regresa la longitud de la lista
        return len(self.__data)

    def pop(self):#Tira y regresa el valor
        if self.is_empty():#try se puede tambien
            print("Fila vacia")
        else:
            return self.__data.pop()
    def push(self,value):
        self.__data.append(value)

    def peek(self):
        return self.__data[len(self.__data)-1]#porque el indice empieza en 0.

    def to_string(self):
        print("-----")
        for item in self.__data[::-1]:#recorre de atras para adelante.
            print(f"| {item} |")
            print("-----")
