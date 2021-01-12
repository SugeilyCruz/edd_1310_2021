class Queue:
    def __init__(self):
        self.__data= list() #[]

    def is_empty(self):
        return len(self.__data)==0

    def length(self):
        return len(self.__data)

    def enqueue(self, elem):
        self.__data.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string(self):
        cadena=""
        for elem in self.__data:
            cadena = cadena + "|" + str(elem)
        cadena = cadena +"|"
        return cadena

# tarea PriorityQueue
class PriorityQueue:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def enqueue(self, prioridad, elem, entrada = 0):
        if len(self.__data) ==  0:
            self.__data.append( [prioridad, elem, entrada] )
        else:
            if  elem not in self.__data:
                for i in self.__data:
                    if prioridad == i[0]:
                        entrada += 1
                self.__data.append( [prioridad, elem, entrada] )
            self.__data = sorted(self.__data, key = lambda x: (x[0], x[2])) #Ordena con prioridad y entrada.

    def dequeue(self):
        if not self.is_empty():
            return print(self.__data.pop(0)[1])
        else:
            print("\n----El barco ya ha sido evacuado por completo-----")

    def to_str(self):
        for item in self.__data:
            print(f'|\t{item[0]}-{item[1]} \t|')
        print('\n')

class BoundedPriorityQueue:
    def __init__(self, niveles):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def length(self):
        return self.__size

    def enqueue(self, prioridad, elem):
        if prioridad < len(self.__data) and prioridad >= 0:
            self.__data[prioridad].enqueue(elem)
            self.__size += 1

    def dequeue(self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size -= 1
                    return print(f"{nivel.dequeue()}\n")
                else:
                    print("No hay nadie en la cola")
        else:
            print("\n----El barco ya ha sido evacuado por completo-----")

    def to_string(self):
        print("Cola:")
        for nivel in range(len(self.__data)):
            print(f" Nivel {nivel} --> { self.__data[nivel].to_string() } " )
