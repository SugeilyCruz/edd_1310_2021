from arrays import Array
with open( 'junio.dat', 'r' ) as txt: #with me ahorra código pero es lo mesmo lo mesmo
    rows = txt.readlines()
    rows = [ r.replace(' ','').strip().split(',') for r in rows ]  #List comprehension
leer=len(rows)
extra=float(276.5)
td=Array(leer)
for x in range(0,leer,1):
    td.set_item(rows[x],x)
    x=x+1
for x in td:
    print(x)
print("\n-------S U E L D O S-------")
for y in range(1,leer,1):
    ml=int(td.get_item(y)[4])
    ant=int(td.get_item(y)[6])
    sl=int(td.get_item(y)[5])
    lm=ml*extra
    to=sl+lm
    tna=float((((2020-ant)*0.03)*sl)+to)
    print(f"{rows[y][1]} tiene un sueldo de {tna}")
    y=y+1
print("\n-------TRABAJADOR CON MAYOR ANTIGUEDAD------- ")
for i in range(1,leer,1):
        if int(td.get_item(i)[6]) == 2016:
            print(td.get_item(i))
        i=i+1
print("\n-------TRABAJADOR CON MENOR ANTIGUEDAD------- ")
for o in range(1,leer,1):
        if int(td.get_item(o)[6]) == 2020:
            print(td.get_item(o))
        o=o+1
