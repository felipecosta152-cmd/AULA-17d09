







#15. Peça números ao usuário até que ele digite 0. Ao final, 
# informe quantos números positivos foram digitados.


count_positivo=0
while True:
    
    numero = int(input("digite um numero (ou 0 para sair ): "))      
    #      if == 0 armazena o valor, se for zero, ele encerra o loop, se for positivo, 
    #   ele soma 1 ao count_positivo.
    
    if numero == 0:
        
        break
    
    if numero > 0:
        
        count_positivo += 1    #count_positivo serve para contar quantos números positivos foram digitados;
        
print(f"Quantidade de números positivos digitados: {count_positivo}")