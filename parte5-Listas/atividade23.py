lista_numeros = [10, 20, 30, 40, 50]

maior_valor = lista_numeros[0]  # começa supondo que o primeiro é o maior

for numero_atual in lista_numeros:
    
    
    if numero_atual > maior_valor:
        
        
        maior_valor = numero_atual  # achou um número maior, atualiza

print("Maior valor:", maior_valor)