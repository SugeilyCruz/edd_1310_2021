from backtracking import LaberintoADT

pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))

lab = LaberintoADT( 6, 6, pasillos_inicial, (5,2), (2,5) )
print(lab.buscar_entrada())
print(lab.resolver_laberinto())
lab.to_string()
while(lab.get_pos_actual(lab.get_pos_actual()[0],lab.get_pos_actual()[1])):
    lab.resolver_laberinto()
lab.to_string()
