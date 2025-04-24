import random

#tamanho da matriz
n = 10

#valores aleatórios entre 0 e 1
matriz = [[random.randint(0,100) for _ in range(n)] for _ in range(n)]

print("Matriz: ")
for linha in matriz:
    print(linha)

naonulas = 0

for i in range(n):
    for j in range(n):
        if matriz[i][j] != 0:
            naonulas += 1

print(f"Número de posição não nulas na matriz: {naonulas}")

