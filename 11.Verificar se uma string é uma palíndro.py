# Verificar se uma string é uma palíndrome 
# Palíndromo, segundo o dicionário Houaiss, “diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para direita ou vice-versa”: osso, Ana, radar, Renner

import string
#importa o módulo string do Python.Uma sequência de caracteres, e esses métodos fornecem diversas operações para realizar tarefas como busca, substituição, concatenação, entre outras, em strings.

palavra = input("Digite uma palavra: ") 
inversa = string[::-1] 
if palavra == inversa: 
    print("É uma palindrome.") 
else: 
   print("Não é uma palindrome.")
