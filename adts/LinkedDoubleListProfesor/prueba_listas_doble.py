from listtwo import LinkedDoubleList

ld= LinkedDoubleList()
print(f"Esta vacia? {ld.is_empty()}")
ld.append(10)
ld.append(20)
ld.append(30)
print(f"La lista tiene {ld.get_size()} elementos")
ld.transversal()
ld.reverse_transversal()
