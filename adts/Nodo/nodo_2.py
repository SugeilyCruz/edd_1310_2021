class Nodo:  # Agregar nodos sin .siguiente
    def __init__(self, dato,sig=None):
        self.dato = dato
        self.siguiente = sig

# EJEMPLO 1
a = Nodo(10)
# EJEMPLO 2 RECONSTRUCCION
a = Nodo(10, Nodo(20))
a = Nodo(10, Nodo(20, Nodo(30)))
a = Nodo(10, Nodo(20, Nodo(30, Nodo(40))))
a = Nodo(10, Nodo(20, Nodo(30, Nodo(40, Nodo(50)))))

# Corrido Transversal
curr_node = a
print(curr_node.dato, "==>", end="")
while(curr_node.siguiente != None):
    curr_node = curr_node.siguiente
    print(curr_node.dato, "==>", end="")
print("")
