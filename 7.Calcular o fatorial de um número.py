# Calcular o fatorial de um número

num = int(input("Digite um número para fazer seu fatorial: "))
#int: inteiro

#condição de uma expressão lógica
if num>=0:
    fatorial = 1

    #laço de repetição
    for i in range (1, num + 1):
        fatorial *= i

        #imprimindo
        print("O fatorial de", num, "é:", fatorial)

else:
#expressão lógica falsa
    print("Entrada inválida! ")