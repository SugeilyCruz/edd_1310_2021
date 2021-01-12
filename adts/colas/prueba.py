from colas import Queue,BoundedPriorityQueue,PriorityQueue

print("...............................................................................")
print("Pruebas de las colas")
print("...............................................................................")

q1= Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print ("Prueba 2 de Queue")
c1={"id": 1,"nombre": "Mario", "balance": 20.5}
c2={"id": 2,"nombre": "Diana", "balance": 3456.5}
c3={"id": 3,"nombre": "Bartolo", "balance": 1000000.0}

atencion= Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente= atencion.dequeue()
print(f"Bienvenido Sr.{siguiente['nombre']}, en que podemos servirle el dia de hoy")
print(atencion.to_string())
print("")

print("...............................................................................")
print("Pruebas de las colas con prioridad acotada")
print("...............................................................................")

maestre = {"prioridad":4 , "descripción":"Maestre","persona":"juan P"}
ninos = {"prioridad":2 , "descripción":"Niños","personas":["Santi H","Ángel H"]}
mecanico = {"prioridad":4 , "descripción":"Mecánico","persona":"Mario Z"}
mujeres = {"prioridad":3 , "descripción":"Mujeres","personas":["Elizabeth R","Samatha C"]}
terceraEdad = {"prioridad":2 , "descripción":"3ra edad","personas":["Rodolfo F","Susana L"]}
ninas = {"prioridad":1 , "descripción":"Niñas","personas":["Sugeily C","Mariana M"]}
hombres = {"prioridad":3 , "descripción":"Hombres","personas":["Victor C","Eduardo G"]}
vigia = {"prioridad":4 , "descripción":"Vigia","persona":"Juan C"}
capitan = {"prioridad":5 , "descripción":"Capitan","persona":"Cid C"}
timonel = {"prioridad":4 , "descripción":"Timonel","persona":"Sebastian W"}

cp = BoundedPriorityQueue(7)
cp.enqueue(maestre['prioridad'], maestre)
cp.enqueue(ninos['prioridad'], ninos)
cp.enqueue(mecanico['prioridad'], mecanico)
cp.enqueue(mujeres['prioridad'], mujeres)
cp.enqueue(terceraEdad['prioridad'], terceraEdad)
cp.enqueue(ninas['prioridad'], ninas)
cp.enqueue(hombres['prioridad'], hombres)
cp.enqueue(vigia['prioridad'], vigia)
cp.enqueue(capitan['prioridad'], capitan)
cp.enqueue(timonel['prioridad'], timonel)

cp.to_string()
print("")
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
cp.dequeue()
print("")

print("...............................................................................")
print("Pruebas de las colas con prioridad no acotada")
print("...............................................................................")

q1 = PriorityQueue()
print("")
q1.enqueue(4, "Maestre")
q1.enqueue(2, "Ninos")
q1.enqueue(4, "Mecanico")
q1.enqueue(3, 'Hombres')
q1.enqueue(4, "Vigia")
q1.enqueue(5, "Capitan")
q1.enqueue(4, "Timonel")
q1.enqueue(3, "Mujeres")
q1.enqueue(2, "3ra edad")
q1.enqueue(1, "Ninas")
q1.to_str()
print("")
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
