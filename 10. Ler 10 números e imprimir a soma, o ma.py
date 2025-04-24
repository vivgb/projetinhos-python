# Ler 10 números e imprimir a soma, o maior e o menor

numeros = [] 
# Cria-se uma lista vazia chamada numeros. Essa lista será usada para armazenar os números fornecidos pelo usuário.

for i in range(10): 
    #loop "for" para solicitar para o usuàrio insira 10 números

     num = int(input("Digite um número: "))
     numeros.append(num)
     # número inserido pelo usuário é adicionado à lista numeros usando o método append()

soma = sum(numeros) 
#A função max() é usada para encontrar o maior número na lista numeros. O resultado é armazenado na variável maior.

maior = max(numeros)
#A função max() é usada para encontrar o maior número na lista numeros. O resultado é armazenado na variável maior.
 
menor = min(numeros) 
#A função min() é usada para encontrar o menor número na lista numeros. O resultado é armazenado na variável menor.

#Mensagem descritiva
print("Soma:", soma) 
print("Maior:", maior) 
print("Menor:", menor)