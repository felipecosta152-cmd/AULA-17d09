#12. Peça números ao usuário e vá somando. 
# Quando ele digitar 0, pare e exiba a soma.

soma = 0

while True:   #True inicia o codigo while até digitar o false. 
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break    #encerrarprograma
    soma += numero

print("A soma é:", soma)
