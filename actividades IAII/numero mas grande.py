import random

# Matriz de ejemplo
matriz = [
    [1, 5, 3],
    [8, 2, 7],
    [4, 9, 6]
]

# Tamaño de la población y número de generaciones
pop_size = 20
n_generations = 100

# Función objetivo (evaluación del individuo)
def fitness(individual):
    i, j = individual
    return matriz[i][j]

# Generar individuo aleatorio
def generate_individual(rows, cols):
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

# Generar población inicial
def generate_population(pop_size, rows, cols):
    return [generate_individual(rows, cols) for _ in range(pop_size)]

# Función de selección (torneo)
def selection(population, n_parents):
    parents = []
    for _ in range(n_parents):
        tournament = random.sample(population, 3)
        winner = max(tournament, key=fitness)
        parents.append(winner)
    return parents

# Función de cruce (intercambio de posiciones)
def crossover(parents):
    parent1, parent2 = parents
    i1, j1 = parent1
    i2, j2 = parent2

    if random.random() < 0.5:
        child = (i1, j2)
    else:
        child = (i2, j1)

    return child

# Función de mutación (mutación de una posición)
def mutation(child, rows, cols):
    i, j = child
    if random.random() < 0.1:
        i = random.randint(0, rows - 1)
    if random.random() < 0.1:
        j = random.randint(0, cols - 1)
    return (i, j)

# Algoritmo genético
def genetic_algorithm(pop_size, n_generations, matriz):
    rows = len(matriz)
    cols = len(matriz[0])

    population = generate_population(pop_size, rows, cols)

    for gen in range(n_generations):
        parents = selection(population, 2)
        children = [crossover(parents) for _ in range(pop_size - len(parents))]
        children = [mutation(child, rows, cols) for child in children]
        population = parents + children

        # Obtener el mejor individuo de la generación
        best_individual = max(population, key=fitness)
        print(f"Generación {gen+1}: Mejor valor = {fitness(best_individual)}, Posición = {best_individual}")

    best_individual = max(population, key=fitness)
    return best_individual

if __name__ == "__main__":
    best_solution = genetic_algorithm(pop_size, n_generations, matriz)
    i, j = best_solution
    max_value = matriz[i][j]
    print(f"La posición del número máximo {max_value} en la matriz es ({i}, {j})")
