from array2D import Array2D

class Juego:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0

    def __init__(self, rens, cols, generaciones, poblacion):
        self.largo = cols
        self.alto = rens
        self.grid = Array2D(self.alto, self.largo, 0)
        self.generaciones = generaciones

        for celula in poblacion:
            # recorre el eje x & y
            self.grid.set_item(celula[0], celula[1], self.CELULA_VIVA)

    def generacioness(self):
        return self.generaciones

    def configura_generacion(self, nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0], celula[1], self.CELULA_VIVA)

    def imprime_grid(self):
        for r in range(self.grid.get_num_rows()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r, c) == 0:
                    print("0", end="")
                else:
                    print("1", end="")
            print("")

    def get_num_rows(self):
        return self.alto

    def get_num_cols(self):
        return self.largo

    def set_celula_muerta(self, row, col):
        self.grid.set_item(row, col, self.CELULA_MUERTA)

    def set_celula_viva(self, row, col):
        self.grid.set_item(row, col, self.CELULA_VIVA)

    def get_is_viva(self, row, col):
        return self.grid.get_item(row, col) == self.CELULA_VIVA

    def get_is_muerta(self, row, col):
        return self.grid.get_item(row, col) == self.CELULA_MUERTA

    def get_numero_vecinos_vivos(self , row , col ):
        limites=[ row-1 , row+1 , col-1 , col+1 ]
        vecinos = 0
        if row >= 0 and row <= self.alto-1 and col >= 0 and col <= self.largo -1 :
            for r in range(limites[0],limites[1]+1):
                for c in range(limites[2],limites[3]+1):
                    if r == self.get_num_rows():#dobla el mapa
                        r = 0
                    if c == self.get_num_cols():#dobla el mapa
                        c = 0
                    if self.get_is_viva(r,c): #compara la celula, si esta viva.
                        vecinos += 1
        if self.get_is_viva(row,col):#Evita que se cuente a sí misma
            vecinos -= 1
        return (vecinos)

    def evolucionar(self):
        lista_clone=[]
#Guarda mi Array2D en mi lista provicional.
        for rw in range( self.grid.get_num_rows() ):
            list_row = []
            for cn in range( self.grid.get_num_cols() ):
                list_row.append( self.grid.get_item(rw, cn) )
            lista_clone.append(list_row)
#recorre cada celula de get_numero_vecinos_vivos y porfa la nueva_generacion.
        for rws in range(self.grid.get_num_rows()):
            for cl in range(self.grid.get_num_cols()):
#1. Si una célula esta viva y tiene 2 o 3 vecinos vivos, la célula sobrevive en la siguiente generación.
                if self.get_is_viva(rws,cl) and (self.get_numero_vecinos_vivos(rws,cl) == (2 or 3)):
                    lista_clone[rws][cl]= self.CELULA_VIVA
#2. Las células vivas que tienen 1 o 0 vecinos vivos, muere por soledad.
                if self.get_is_viva(rws,cl) and (self.get_numero_vecinos_vivos(rws,cl) <= 1):
                    lista_clone[rws][cl]= self.CELULA_MUERTA
#3. Una célula viva que tiene 4 o mas vecinos vivos, muere por sobrepoblación.
                if self.get_is_viva(rws,cl) and (self.get_numero_vecinos_vivos(rws,cl) >= 4):
                    lista_clone[rws][cl]= self.CELULA_MUERTA
#4. Una célula muerta que tiene exactamente 3 vecinos vivos resulta en un nacimiento en la siguiente generación.
                if self.get_is_muerta(rws,cl) and self.get_numero_vecinos_vivos(rws,cl)== 3 :
                    lista_clone[rws][cl]= self.CELULA_VIVA
#Reemplaza los datos de array2d con los de la lista provicional.
        for r_i in range( len(lista_clone) ):
            for c_i in range( len(lista_clone[r_i])):
                self.grid.set_item( r_i, c_i, lista_clone[r_i][c_i])
