algoritmo "teste VSCODE"
var
   x: caractere
   n1, n2, soma: inteiro

inicio
   escreval("Qual seu nome?")
   leia(x)

   soma <- 0

   enquanto soma <> 10 faca
      escreval("Digite um número:")
      leia(n1)
      escreval("Digite outro:")
      leia(n2)
      soma <- n1 + n2
      escreval("Soma atual: ", soma)
   fimenquanto

   escreval("Chegou a 10!")
fimalgoritmo