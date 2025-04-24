
distance_matrix = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 11, 80],
    [5, 17, 11, 0, 80],
    [12, 28, 80, 80, 0]
]

# Part (a)
def find_distance(x, y):
    return distance_matrix[x-1][y-1]

# Part (b)
def calculate_total_distance():
    path = []
    while True:
        city = int(input("Entre com a cidade (1-5) ou 0 para encerrar: "))
        if city == 0:
            break
        path.append(city)
    
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += find_distance(path[i], path[i+1])
    
    return total_distance

# Example usage for part (a)
x = int(input("Entre com a cidade X (1-5): "))
y = int(input("Entre com a cidade Y (1-5): "))
print(f"A distancia entre a cidade {x} e a cidade {y} é {find_distance(x, y)} km")

# Example usage for part (b)
print(f"O total da distancia entre o caminho é {calculate_total_distance()} km")