import random
import string

# Cadena objetivo
target_string = "HELLO WORLD"

# Tamaño de la población y longitud de la cadena objetivo
pop_size = 20
str_length = len(target_string)

# Función objetivo (evaluación del individuo)
def fitness(individual):
    return sum(1 for a, b in zip(individual, target_string) if a == b)

# Generar individuo aleatorio
def generate_individual(length):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(length))

# Generar población inicial
def generate_population(pop_size, str_length):
    return [generate_individual(str_length) for _ in range(pop_size)]

# Función de selección (ruleta)
def selection(population, fitness_scores, n_parents):
    parents = random.choices(population, weights=fitness_scores, k=n_parents)
    return parents

# Función de cruce (cruce en un punto)
def crossover(parents):
    point = random.randint(1, len(parents[0]) - 1)
    child = parents[0][:point] + parents[1][point:]
    return child

# Función de mutación (mutación de un carácter)
def mutation(child, mutation_rate):
    child = list(child)
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.choice(string.ascii_uppercase + ' ')
    return ''.join(child)

# Algoritmo genético
def genetic_algorithm(pop_size, str_length, n_generations, mutation_rate):
    population = generate_population(pop_size, str_length)

    for gen in range(n_generations):
        fitness_scores = [fitness(individual) for individual in population]
        parents = selection(population, fitness_scores, 2)
        children = [crossover(parents) for _ in range(pop_size - len(parents))]
        children = [mutation(child, mutation_rate) for child in children]
        population = parents + children

        # Obtener el mejor individuo de la generación
        best_individual = max(population, key=fitness)
        print(f"Generación {gen+1}: Mejor puntaje = {fitness(best_individual)}, Individuo = {best_individual}")

        # Si se ha encontrado la cadena objetivo, detener el algoritmo
        if fitness(best_individual) == str_length:
            break

    best_individual = max(population, key=fitness)
    return best_individual

if __name__ == "__main__":
    n_generations = 10
    mutation_rate = 0.1

    best_solution = genetic_algorithm(pop_size, str_length, n_generations, mutation_rate)
    print(f"Solución encontrada: {best_solution}")
