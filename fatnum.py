import math

def fat(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fat(n-1)

num1 = int(input("Insira o 1º número inteiro:"))
num2 = int(input("Insira o 2º número inteiro:"))

if num1 % 2 ==0 and num2 % 2 == 0:
    resul = num1 ** num2
    print(f"A potência de {num1} por {num2} é: {resul}")

elif num1 % 2 !=0 and num2 % 2 !=0:
    resul = fat(num1) + fat(num2)
    print(f"A soma dos fatoriais de {num1} e {num2} é: {resul}")

else:
    if num1 % 2 ==0:
        resul = fat(num1)/ math.sqrt(num2)
    else:
        resul = fat(num1)/ math.sqrt(num2)
    print(f"O fatorial de {num1} dividido pela raiz quadrada de {num2} é: {resul}")
