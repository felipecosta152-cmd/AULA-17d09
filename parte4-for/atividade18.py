#18. Calcule e exiba a soma de todos os números de 1 a 100.


soma = 0 #armazena a soma dos números de 1 a 100.


for numero in range(1, 101):
    soma += numero
print(f"A soma de todos os números de 1 a 100 é: {soma}")