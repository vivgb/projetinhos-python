#calcular os divisores de um número

#declarando a variavel n, significando os números

n = int(input("Digite um número: ")) 

#imprimindo os divisores de determinado número
print("Os divisores de" , n, "são:")

for i in range(1, n + 1):
#"for" é um laço de repetição, onde começa com o for, em seguida temos uma variável para indicar o que vamos analisar. É similar com o "para"

     if n % i == 0:
    #if é um comando condicional cujo é realizado apenas se a expressão relacional/lógica for verdadeira.
          print(i,end=" ") 
