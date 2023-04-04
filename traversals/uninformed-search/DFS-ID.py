# create a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfid(graph, start, goal):
    depth_limit = 0
    while True:
        result = dfs(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

def dfs(graph, start, goal, depth_limit, visited=None):
    if visited is None:
        visited = set()  # to keep track of visited vertices
    if start == goal:
        return [start]
    if depth_limit == 0:
        return None
    visited.add(start)
    for next_vertex in graph[start]:
        if next_vertex not in visited:
            result = dfs(graph, next_vertex, goal, depth_limit-1, visited)
            if result is not None:
                return [start] + result
    return None

print(dfid(graph, 'A', 'F'))
