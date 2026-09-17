#5. Peça o preço de um produto e a quantidade comprada. 
# Exiba o valor total, com duas casas decimais.

preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
valor_total = preco * quantidade
print(f"O valor total é: R$ {valor_total:.2f}")

#.2f    DUAS CASAS DECIMAIS