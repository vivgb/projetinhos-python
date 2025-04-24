#crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado; 
# (2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.

import math

num = float(input('Digite um valor:'))
if num >= 1 and num <= 3:
    print(num**2)
elif num == 4 or num ==9:
    print (math.sqrt(num))
elif num == 6 or num ==7 or num ==8:
    print(num/9.0)