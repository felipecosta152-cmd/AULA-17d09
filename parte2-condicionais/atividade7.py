#7. Peça dois números e exiba qual é o maior. Se forem 
# iguais, informe isso.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    
    
    print(f"O primeiro número ({numero1}) é o maior.")
elif numero2 > numero1:
    # se, senao, condição. 
    
    print(f"O segundo número ({numero2}) é o maior.")
else:
    
    print("Os números são iguais.")

    
    #________________________________________________________