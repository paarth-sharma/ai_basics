import copy

# function to find the location of the blank tile
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# function to calculate the heuristic value (number of misplaced tiles)
def heuristic(puzzle, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                count += 1
    return count

# function to generate all possible successor states
def generate_successors(puzzle):
    successors = []
    i, j = find_blank(puzzle)
    if i > 0:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[i][j], new_puzzle[i-1][j] = new_puzzle[i-1][j], new_puzzle[i][j]
        successors.append(new_puzzle)
    if i < 2:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[i][j], new_puzzle[i+1][j] = new_puzzle[i+1][j], new_puzzle[i][j]
        successors.append(new_puzzle)
    if j > 0:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[i][j], new_puzzle[i][j-1] = new_puzzle[i][j-1], new_puzzle[i][j]
        successors.append(new_puzzle)
    if j < 2:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[i][j], new_puzzle[i][j+1] = new_puzzle[i][j+1], new_puzzle[i][j]
        successors.append(new_puzzle)
    return successors

# function to perform the hill-climbing algorithm
def hill_climbing(puzzle, goal):
    current = puzzle
    while True:
        print("Current state:")
        for row in current:
            print(row)
        print()
        h = heuristic(current, goal)
        if h == 0:
            return current
        successors = generate_successors(current)
        best_successor = current
        best_h = h
        for successor in successors:
            successor_h = heuristic(successor, goal)
            if successor_h < best_h:
                best_successor = successor
                best_h = successor_h
        if best_h >= h:
            return None
        current = best_successor

# example usage
initial_state = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
result = hill_climbing(initial_state, goal_state)
if result is None:
    print("No solution found")
else:
    print("Solution found:")
    for row in result:
        print(row)
