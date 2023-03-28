import random
import math

# Function to check if a given solution satisfies all clauses in the formula
def satisfies(solution):
    a, b, c, d = solution
    if (not a or d) and (c or b) and (not c or not d) and (not d or not b) and (not a or not d):
        return True
    return False

# Function to generate a new solution by randomly flipping the value of one variable
def movegen(solution):
    index = random.randint(0, 3)
    new_solution = solution.copy()
    new_solution[index] = not new_solution[index]
    return new_solution

# Function to evaluate a solution based on the number of clauses it satisfies
def evaluate(solution):
    score = 0
    if (not solution[0] or solution[3]): score += 1
    if (solution[2] or solution[1]): score += 1
    if (not solution[2] or not solution[3]): score += 1
    if (not solution[3] or not solution[1]): score += 1
    if (not solution[0] or not solution[3]): score += 1
    return score

# Simulated Annealing algorithm
def simulated_annealing(initial_solution, T, cooling_function, random_numbers):
    current_solution = initial_solution
    current_score = evaluate(current_solution)
    best_solution = current_solution.copy()
    best_score = current_score

    for i in range(1, T+1):
        T = cooling_function(T)
        temperature = T / math.log(i+1)

        # generate a new solution
        new_solution = movegen(current_solution)
        new_score = evaluate(new_solution)

        # accept good moves and accept bad moves with a certain probability
        delta = new_score - current_score
        if delta >= 0:
            current_solution = new_solution
            current_score = new_score
            if current_score > best_score:
                best_solution = current_solution.copy()
                best_score = current_score
        else:
            probability = math.exp(delta / temperature) if delta > 0 else 0
            if probability > random_numbers[i % 3]:
                current_solution = new_solution
                current_score = new_score

    return best_solution, best_score

# Initial population
initial_solution = [True, True, True, True]

# Simulated Annealing parameters
T = 500
cooling_function = lambda t: t - 50
random_numbers = [0.655, 0.254, 0.432]

# Run Simulated Annealing algorithm
best_solution, best_score = simulated_annealing(initial_solution, T, cooling_function, random_numbers)

# Print the results
print("Best solution:", best_solution)
print("Best score:", best_score)
