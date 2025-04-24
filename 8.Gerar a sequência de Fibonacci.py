# Gerar a sequência de Fibonacci
n = int(input("Digite o número: "))
print("Sua Sequência de Fibonacci") 

#declarando o valor das variaveis

fib1 = 0 
fib2 = 1 
#São variáveis que armazenam os dois primeiros números da sequência de Fibonacci

print(fib1,end=" ")
print(fib2,end=" ") 
for i in range(2, n):
 #Este loop começa a partir de 2 porque já temos os dois primeiros números (fib1 e fib2) armazenados.
 #Precisa gerar n - 2 números adicionais para obter uma sequência de Fibonacci completa até o número n especificado pelo usuário.
   fib = fib1 + fib2  
   fib1 = fib2
   fib2 = fib 

   #Imprime o próximo número da sequência de Fibonacci.
   print(fib,end=" ")
