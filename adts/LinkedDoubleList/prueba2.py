from listas2 import LinkedDoubleList

l=LinkedDoubleList()#Creo mi Lista doblemente ligada
l.append(10)
l.append(5)
l.append(3)
l.append(15)
l.append(20)
l.append(3)
l.append(5)
l.append(1)
print(f"L esta vacia? {l.is_empty()}")#Regresa True si esta vacia.
print(f"size=> {l.get_size()}")#Total de Nodos

print("")
l.transversal()
l.reverse_transversal()
print("")

l.remove_from_head(10)
l.remove_from_tail(1)

l.remove_from_head(5)
l.remove_from_tail(3)

l.transversal()
l.reverse_transversal()

#Imprime conando desde 1.
print("")
l.find_from_head(15)
l.find_from_tail(20)
print("")
