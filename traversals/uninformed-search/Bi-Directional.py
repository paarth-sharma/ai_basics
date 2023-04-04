from collections import deque

def bidirectional_search(graph, start, goal):
    queue_start = deque([start])
    queue_goal = deque([goal])
    
    global visited_start
    global visited_goal

    visited_start = set([start])
    visited_goal = set([goal])
    
    path_start = {start: None}
    path_goal = {goal: None}
    
    # Main loop
    while queue_start and queue_goal:

        node_start = queue_start.popleft()

        for neighbor in graph[node_start]:

            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append(neighbor)
                path_start[neighbor] = node_start

                if neighbor in visited_goal:
                    path = [neighbor]

                    while node_start:
                        path.append(node_start)
                        node_start = path_start[node_start]
                    
                    path.reverse()
                    node_goal = neighbor
                    
                    while node_goal != goal:
                        path.append(node_goal)
                        node_goal = path_goal[node_goal]
                    return path
        
        # goal node
        node_goal = queue_goal.popleft()
        
        for neighbor in graph[node_goal]:
        
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append(neighbor)
                path_goal[neighbor] = node_goal
        
                if neighbor in visited_start:
                    # Path found!
                    path = [neighbor]
        
                    while node_goal:
                        path.append(node_goal)
                        node_goal = path_goal[node_goal]
        
                    path.reverse()
                    node_start = neighbor
        
                    while node_start != start:
                        path.insert(0, node_start)
                        node_start = path_start[node_start]
                    return path
    
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

start = 'A'
goal = 'G'

path = bidirectional_search(graph, start, goal)

if path:
    print("Visited nodes from start:", list(visited_start))
    print("Visited nodes from goal:", list(visited_goal))
    print("Path found:", path)
else:
    print("No path found.")
