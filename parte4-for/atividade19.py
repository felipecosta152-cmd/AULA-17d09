#atividade, peça um numero e diga seu fatorial: ex> fatorial de 5 é 5x5x4x3x2x1 = 120 

fatorial = int(input("Digite o primeiro número:"))
for i in range(1, fatorial + 1):
    
    fatorial *= i  #i é o contador do loop, que vai de 1 até o número digitado pelo usuário.
    #* significa multiplicação, e o operador *= forma abreviada de fatorial = fatorial * i. 
print(f"O fatorial é: {fatorial}")
