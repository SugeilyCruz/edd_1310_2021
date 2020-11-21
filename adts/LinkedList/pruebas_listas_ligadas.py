from listas import LinkedList

l= LinkedList()
print(f"L esta vacia? {l.is_empty()}")#pregunta si head tiene None o tiene value. si es None regresa True, si no False.
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f"L esta vacia? {l.is_empty()}")
l.transversal()
l.remove(5)
l.add_before(10,15)
l.transversal()
l.add_after(15,3)
l.transversal()
l.preppend(3)
l.transversal()
print(l.tail())
print(l.get(0))
""" x=l.tail() 
print(x.data)
print(l.get()) """
