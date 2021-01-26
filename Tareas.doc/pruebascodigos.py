def remove(self, value):
    encontrado= self.search(value)#introducir el metodo search hasta que encuente el no y seguir con lo de abajo.
    #caso 1
    if encontrado.left == None and encontrado.right ==None:
        print("Eliminando", encontrado.data)
        self.search(value) == None
    #caso 2
    elif (encontrado.left != None and encontrado.right == None) or \
    (encontrado.left == None and encontrado.right != None):
        print(f"Encontrado: {encontrado.data}")
