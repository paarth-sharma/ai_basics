import random

# Item data
items = {
    'A': {'weight': 2, 'value': 3},
    'B': {'weight': 3, 'value': 5},
    'C': {'weight': 4, 'value': 7},
    'D': {'weight': 5, 'value': 9}
}

# Max weight capacity
max_weight = 9

# Genetic Algorithm Parameters
population_size = 4
chromosome_size = 4
mutation_order = ['XC', 'XA', 'XD', 'XB']

# Function to generate initial population
def generate_population():
    population = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_size):
            chromosome.append(random.randint(0, 1))
        population.append(chromosome)
    return population

# Function to calculate fitness of a chromosome
def calculate_fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(chromosome_size):
        if chromosome[i] == 1:
            item = 'ABCD'[i]
            total_weight += items[item]['weight']
            total_value += items[item]['value']
    if total_weight > max_weight:
        total_value = 0
    return total_value

# Function to perform one-point crossover
def one_point_crossover(chromosome1, chromosome2):
    crossover_point = len(chromosome1) // 2
    offspring1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    offspring2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    return offspring1, offspring2

# Function to perform mutation
def mutate(chromosome):
    for bit in mutation_order:
        index = 'ABCD'.index(bit[1])
        if bit[0] == '1':
            chromosome[index] = 1 - chromosome[index]
    return chromosome

# Function to perform selection, crossover and mutation for next generation
def next_generation(population):
    # Calculate fitness of all chromosomes
    fitness = []
    for chromosome in population:
        fitness.append(calculate_fitness(chromosome))

    # Select two fittest chromosomes
    fittest_indices = sorted(range(len(fitness)), key=lambda k: fitness[k], reverse=True)[:2]
    next_population = [population[i] for i in fittest_indices]

    # Perform crossover and mutation on third and fourth fittest chromosomes
    offspring1, offspring2 = one_point_crossover(population[2], population[3])
    offspring1 = mutate(offspring1)
    next_population.extend([offspring1, population[3]])

    # Return next generation
    return next_population

# Main program
population = generate_population()

for i in range(4):
    print("Iteration", i+1, "Population:", population)
    population = next_generation(population)

# Final population after 4 iterations
print("Final Population:", population)
