# Calcular as raízes de uma equação do segundo grau 

import math 
import cmath
#Import é usada para acessar e utilizar código definido em outros arquivos ou bibliotecas. Ela permite que você inclua funcionalidades em seus softwares.

print("Digite as informações necessárias para calcular uma equação do segundo grau.")
# Entrada dos dados 
a = float(input("a:")) 
b = float(input("b:")) 
c = float(input("c:"))

#float: tipo de variavel para números reais 
#input: é utilizado para declarar e armazenar a variavel de forma que já imprima

if a==0: 
    #if é um comando condicional cujo é realizado apenas se a expressão relacional/lógica for verdadeira.

    print("Não é uma equação do segundo grau!!!") 
    #print para imprimir

    #se a expressão relacional/lógica NÃO for verdadeira
else: 
    delta = b**2 - 4*a*c 
if delta < 0:         # Raízes complexas 
    x1= (-b + cmath.sqrt(delta))/(2*a) 
    x2= (-b - cmath.sqrt(delta))/(2*a) 
    print("Raizes complexas:", x1, "e", x2)


#elif: caso não seja verdadeira a expressão relacional,mas, sim, tiver outra condição

elif delta == 0: #   Apenas uma raiz 
    x = -b / (2*a) 
    print("Uma raiz real:", x) 
else:                # Duas raízes
    x1 = (-b + math.sqrt(delta)) / (2*a) 
    x2 = (-b - math.sqrt(delta)) / (2*a) 

    #imprimir o resultado
    print("Duas raízes reais:", x1, "e", x2)
