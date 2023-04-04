# create a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dls(graph, start, goal, depth_limit, depth=0, visited=None):
    if visited is None:
        visited = set()  # to keep track of visited vertices
    if start == goal:
        return [start]
    if depth == depth_limit:
        return None
    visited.add(start)
    for next_vertex in graph[start]:
        if next_vertex not in visited:
            result = dls(graph, next_vertex, goal, depth_limit, depth+1, visited)
            if result is not None:
                return [start] + result
    return None

def dldfs(graph, start, goal, max_depth):
    result = None
    for depth_limit in range(max_depth+1):
        result = dls(graph, start, goal, depth_limit)
        if result is not None:
            break
    return result

max_depth = int(input("Enter the maximum depth limit: "))

result = dldfs(graph, 'A', 'F', max_depth)
if result is not None:
    print(result)
else:
    print("No path found within the maximum depth limit.")
