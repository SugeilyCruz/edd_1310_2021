print("Crear una lista de enteros en Python y realizar la suma con recursividad, el caso base es cuando la lista este vacia.")
def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def main():
    datos= [4,2,3,5]#14
    dt= [4,2,3,5]
    res=suma_lista_rec(datos)
    print(f"\tLista: {dt} Suma total: {res}\n")
main()

print("Hacer una función recurso que dado un número entero positivo,imprima a la salida una cuenta regresiva hasta cero.")
def regresiva(num):
    if num >=0:
        print(f"\t\t\t{num}")
        regresiva(num-1)

def main2():
    num=5
    print(f"\t\tNumero ingresado: {num}")
    regresiva(num)
main2()

print("Hacer una función recursiva que reciba de entrada una pila con al menos 3 elementos y con recursividad elimine el elemento en la posición media.")
def deleteMid(pila, curr=1) :
    middle=round((pila.length()+curr) /2)
    if (pila.is_empty()):
        return
    else:
        if (curr != middle):
            n = pila.peek()
            pila.pop()
            deleteMid(pila, curr= curr+1)
            pila.push(n)
        else:
            print(f"Valor medio de la pila: {pila.peek()}")
            pila.pop()

from pilas import Stack
def main3():
    st = Stack()
    st.push('q')
    st.push('u')
    st.push('e')
    st.push('s')#eliminar
    st.push('i')
    st.push('t')
    st.push('o')
    print("---Pila inicial---")
    st.to_string()
    print("---Pila Nueva---")
    deleteMid(st)
    st.to_string()

main3()
