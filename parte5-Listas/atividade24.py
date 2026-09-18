#24. Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.


lista = [5, 12, 8, 20, 3, 15]

contador = 0

for item in lista:
    
    if item > 10:
        
        contador += 1

print("Quantidade de itens maiores que 10:", contador)