import copy
import heapq

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

# function to perform the best-first-search algorithm
def best_first_search(puzzle, goal):
    explored = set()
    heap = [(heuristic(puzzle, goal), puzzle)]
    while heap:
        _, current = heapq.heappop(heap)
        explored.add(tuple(map(tuple, current)))
        print("Current state:")
        for row in current:
            print(row)
        print()
        if current == goal:
            return current
        successors = generate_successors(current)
        for successor in successors:
            if tuple(map(tuple, successor)) not in explored:
                heapq.heappush(heap, (heuristic(successor, goal), successor))
    return None

# example usage
initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
result = best_first_search(initial_state, goal_state)
if result is None:
    print("No solution found")
else:
    print("Solution found:")
    for row in result:
        print(row)
