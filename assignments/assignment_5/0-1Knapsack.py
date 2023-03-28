import random

# item names, weights and values
items = {
    "A": {"weight": 45, "value": 3},
    "B": {"weight": 40, "value": 5},
    "C": {"weight": 50, "value": 8},
    "D": {"weight": 90, "value": 10}
}

# chromosome length
chromosome_length = 4

# maximum weight capacity of the bag
max_weight = 100

# initial population
population = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

# fitness function
def fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(chromosome_length):
        if chromosome[i] == 1:
            item = "ABCD"[i]
            total_weight += items[item]["weight"]
            total_value += items[item]["value"]
    if total_weight > max_weight:
        return 0
    else:
        return total_value

# selection function
def selection(population):
    fitness_scores = [fitness(chromosome) for chromosome in population]
    fittest1 = population[fitness_scores.index(max(fitness_scores))]
    fitness_scores.remove(max(fitness_scores))
    fittest2 = population[fitness_scores.index(max(fitness_scores))]
    return fittest1, fittest2

# crossover function
def crossover(parent1, parent2):
    crossover_point = chromosome_length // 2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring1

# mutation function
def mutation(chromosome):
    mutation_bits = [3, 2, 1, 0]
    mutated_chromosome = chromosome.copy()
    
    for bit in mutation_bits:
        mutated_chromosome[bit] = 1 - mutated_chromosome[bit]
    return mutated_chromosome

# running algo for 10 iterations
for i in range(10):
    # selection
    fittest1, fittest2 = selection(population)

    # crossover
    offspring1 = crossover(fittest1, fittest2)

    # mutation
    offspring1 = mutation(offspring1)

    # replace least fit chromosome with offspring1
    fitness_scores = [fitness(chromosome) for chromosome in population]
    least_fit_index = fitness_scores.index(min(fitness_scores))
    population[least_fit_index] = offspring1

# output final fittest chromosome
fitness_scores = [fitness(chromosome) for chromosome in population]
fittest_index = fitness_scores.index(max(fitness_scores))
fittest_chromosome = population[fittest_index]
print("Fittest chromosome:", fittest_chromosome)
print("Fitness score:", fitness(fittest_chromosome))