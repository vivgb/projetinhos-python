# Imprimir a tabuada de um número 
continua = True
#Isso define uma variável continua como True. Essa variável será usada para controlar se o programa deve continuar ou não a executar.

while continua: 
    #Isso inicia um loop "while"(enquanto) que continua enquanto a variável continua for verdadeira.

  n = int(input("Digite um número: "))
  for i in range(1, 11):
        #Loop "for" que itera de 1 a 10 (inclusive). Ele será usado para gerar a tabuada do número fornecido pelo usuário.

      print(n, "x", i, "=", n*i) 

  resposta=input("Deseja continuar (s/n)?")
  #Com o input a resposta é armazenada na variável resposta.

  if resposta=="n": 
     continua=False

     #Se o usuário digitar "n", a variável continua é definida como False, o que faz com que o loop while seja encerrado.
     #E o programa termina. Se o usuário digitar qualquer outra coisa além de "n", o loop continua, e o programa solicita outro número para gerar a tabuada.
