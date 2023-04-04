import heapq

# create a weighted graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(graph, start, goal):
    visited = set()  # to keep track of visited vertices
    queue = [(0, start)]  # to keep track of vertices to be visited, with their cumulative cost
    while queue:
        (cost, vertex) = heapq.heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return cost
            for (next_vertex, next_cost) in graph[vertex]:
                if next_vertex not in visited:
                    heapq.heappush(queue, (cost + next_cost, next_vertex))
    return None

print(ucs(graph, 'A', 'F'))
