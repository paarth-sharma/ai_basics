from queue import PriorityQueue

def ucs(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current_cost, current_node = frontier.get()

        if current_node == goal:
            break

        explored.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost = cost_so_far[current_node] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    frontier.put((priority, neighbor))
                    came_from[neighbor] = current_node

    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()

    return path, cost_so_far[goal]


graph = {
    'S': {'A': 1,'B': 5, 'C': 15},
    'A': {'G': 10},
    'B': {'G': 5},
    'C': {'G': 5}
}

start = 'S'
goal = 'G'

path, cost = ucs(graph, start, goal)

print("Path taken:", path)
print("Total cost:", cost)
