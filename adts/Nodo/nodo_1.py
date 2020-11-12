class Nodo:#Los desencapsulamos para poder borrar, cambiar etc mas facil, no sean privados.
    def __init__( self , dato ):
        self.dato = dato
        self.siguiente = None

#ejemplo 1
a= Nodo(12)
print(a.dato)
#print(a.siguiente)

#Empieza agregar mas elementos
#Ejemplo 2
a.siguiente=Nodo(20)

#Ejemplo 3
a.siguiente.siguiente= Nodo(30)

#Ejemplo 4
a.siguiente.siguiente.siguiente= Nodo(40)

#Ejemplo 5
a.siguiente.siguiente.siguiente.siguiente=Nodo(50)

#Ejemplo 6 Eliminando nodo 30
a.siguiente.siguiente=a.siguiente.siguiente.siguiente # del nodo 20, lo apaunta al 40(el = es como siguiente)

#Ejemplo 7 Cambiar un dato
a.siguiente.siguiente.dato= 45 #cambiamos 40 por 45

#Ejemplo 8 Insertar un dato entre dos.
tmp= a.siguiente.siguiente.siguiente#Respaldo mi nodo 50, para que no se pierda
a.siguiente.siguiente.siguiente=Nodo(48) #creo mi nuevo nodo
a.siguiente.siguiente.siguiente.siguiente= tmp #vuelvo agregar mi nodo 50

#Corrido Transversal
curr_node=a
print(curr_node.dato, "==>", end="")
while(curr_node.siguiente != None):
    curr_node = curr_node.siguiente
    print(curr_node.dato,"==>",end="")
print("")
