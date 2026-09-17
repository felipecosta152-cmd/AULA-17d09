#13. Peça uma senha ao usuário e continue pedindo até que 
# ele digite senai123. 
# Ao acertar, exiba "Acesso liberado".

#O while sempre testa uma condição: 
# enquanto essa condição for True (verdadeira), 
# ele continua repetindo. Quando vira False, ele para.


senha_correta = "senai123"      #senha correta 
senha_digitada = input("Digite a senha: ")       #leitura

while senha_digitada != senha_correta: # ! = diferente de... 

    print("Senha incorreta!")

    senha_digitada = input("Digite a senha novamente: ")

print("Acesso liberado!")
#_____________________________________________________