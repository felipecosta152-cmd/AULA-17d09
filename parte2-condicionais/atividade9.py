#9. Peça a média de um estudante e classifique: 
# acima de 7 aprovado, entre 5 e 7 
# recuperação, abaixo de 5 reprovado. peça 3 notas no mínimo.
print("Digite as notas do estudante:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:


    print("Estudante aprovado.")
elif 5 <= media < 7:


    print("Estudante em recuperação.")
else:


    print("Estudante reprovado.")
    #ESTRUTURA BÁSICA DE CONDIÇÃO