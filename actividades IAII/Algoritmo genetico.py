import random

# Función objetivo (evaluación del individuo)
def fitness(individual):
    return sum(individual)

# Generar individuo aleatorio
def generate_individual(length):
    return [random.randint(0, 100) for _ in range(length)]

# Generar población inicial
def generate_population(pop_size, ind_length):
    return [generate_individual(ind_length) for _ in range(pop_size)]

# Función de selección (torneo)
def selection(population, n_parents):
    parents = []
    for _ in range(n_parents):
        tournament = random.sample(population, 3)
        winner = max(tournament, key=fitness)
        parents.append(winner)
    return parents

# Función de cruce (punto de cruce)
def crossover(parents):
    point = random.randint(1, len(parents[0]) - 1)
    child = parents[0][:point] + parents[1][point:]
    return child

# Función de mutación (mutación de un gen)
def mutation(child):
    gene_to_mutate = random.randint(0, len(child) - 1)
    child[gene_to_mutate] = random.randint(0, 100)
    return child

# Algoritmo genético
def genetic_algorithm(pop_size, ind_length, n_generations):
    population = generate_population(pop_size, ind_length)

    for gen in range(n_generations):
        parents = selection(population, 2)
        children = [crossover(parents) for _ in range(pop_size - len(parents))]
        children = [mutation(child) if random.random() < 0.1 else child for child in children]
        population = parents + children

        # Obtener el mejor individuo de la generación
        best_individual = max(population, key=fitness)
        print(f"Generación {gen+1}: Mejor valor = {fitness(best_individual)}, Individuo = {best_individual}")

    best_individual = max(population, key=fitness)
    return best_individual

if __name__ == "__main__":
    pop_size = 10
    ind_length = 5
    n_generations = 5

    best_solution = genetic_algorithm(pop_size, ind_length, n_generations)
    print(f"Solución óptima encontrada: {best_solution}")
