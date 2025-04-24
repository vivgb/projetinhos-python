#Somar os digitos de um número menor que 100

numero=int(input("Digite um número menor que 100: "))
#int = inteiro

#if é utilizado como caso "se" estiver dentro de certa condição

if numero>=100:
    print("O número deve ser menor que 100.")

#else seria justamente caso não estiver dentro da condição

else:
    dezena = numero//10
    unidade = numero%10
    soma= dezena+unidade

    #impressão das informações

    print("soma: ", soma)
