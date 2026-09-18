# 25. Dada a lista [3, 7, 1, 9, 4], exiba os itens na ordem inversa.
lista = [3, 7, 1, 9, 4]

# Pega a posição do último item da lista
posicao_inicial = len(lista) - 1 #len serve para pegar o tamanho da lista, e subtrai 1 para pegar a posição do último item

# Percorre da última posição até a primeira (de trás para frente)
for posicao_atual in range(posicao_inicial, -1, -1):
    print(lista[posicao_atual])
    
    