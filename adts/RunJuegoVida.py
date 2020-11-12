from juego import Juego

#Gen0
juego = Juego(7, 7, 6, [(1,2), (2,1), (2,2), (2,3)])
juego.imprime_grid()
print("")
#juego.evolucionar()#Metodo de juego, toma el array clonado.
#juego.imprime_grid()#imprime la matriz
#print(juego.get_numero_vecinos_vivos(1,2))#Probar cuadro CelulaViva.
for grc in range(juego.generacioness()):
    print("")
    juego.evolucionar()
    juego.imprime_grid()
