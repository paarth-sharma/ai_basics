# iterative deepening
def dfs_blocks_world_depth_limit(start_state, goal_state, depth_limit):
    visited_states = set()
    stack = [(start_state, [])]
    
    while stack:
        current_state, actions = stack.pop()
        
        if current_state == goal_state:
            return actions
        
        visited_states.add(tuple(map(tuple, current_state)))
        
        if len(actions) >= depth_limit:
            continue
        
        for i, source in enumerate(current_state):
            for j, destination in enumerate(current_state):
                if i != j and source:
                    next_state = [list(block_list) for block_list in current_state]
                    next_state[j].append(next_state[i].pop())
                    
                    if tuple(map(tuple, next_state)) not in visited_states:
                        stack.append((next_state, actions + [(i, j)]))
    
    return None

def iddfs_blocks_world(start_state, goal_state):
    depth_limit = 3
    
    while True:
        print(f"Iteration {depth_limit}:")
        print(*start_state, sep="\n")
        print()
        
        result = dfs_blocks_world_depth_limit(start_state, goal_state, depth_limit)
        
        if result is not None:
            print("Goal State:")
            print(*goal_state, sep="\n")
            print()
            return result
        
        depth_limit += 1


# DFS method
def dfs_blocks_world(start_state, goal_state):
    visited_states = set()
    stack = [(start_state, [])]
    
    while stack:
        current_state, actions = stack.pop()
        
        if current_state == goal_state:
            print("Goal State and current state are equal: ")
            print(*current_state, sep="\n")
            print()
            return actions
        
        visited_states.add(tuple(map(tuple, current_state)))
        
        print("Current State:")
        print(*current_state, sep="\n")
        print()
        
        for i, source in enumerate(current_state):
            for j, destination in enumerate(current_state):
                if i != j and source:
                    next_state = [list(block_list) for block_list in current_state]
                    next_state[j].append(next_state[i].pop())
                    
                    if tuple(map(tuple, next_state)) not in visited_states:
                        stack.append((next_state, actions + [(i, j)]))
    
    return None


# DEPTH LIMITED
def dls_blocks_world(start_state, goal_state, limit):
    visited_states = set()
    stack = [(start_state, [])]

    while stack:
        current_state, actions = stack.pop()
        
        if current_state == goal_state:
            print("Goal state:")
            print(*goal_state, sep='\n')
            return actions
        
        visited_states.add(tuple(map(tuple, current_state)))
        
        if len(actions) >= limit:
            continue
        
        for i, source in enumerate(current_state):
            for j, destination in enumerate(current_state):
                if i != j and source:
                    next_state = [list(block_list) for block_list in current_state]
                    next_state[j].append(next_state[i].pop())
                    
                    if tuple(map(tuple, next_state)) not in visited_states:
                        stack.append((next_state, actions + [(i, j)]))
                        print(f"Iteration {len(actions) + 1}:")
                        print(*next_state, sep="\n")
                        print()
    
    print("Goal state cannot be reached from initial state.")
    return None




start_state = [['A', 'B', 'C', 'D', 'E'], [], []]
goal_state = [[], [], ['C', 'A', 'B', 'D', 'E']]
depth_limit = 3

actions = iddfs_blocks_world(start_state, goal_state)


limit = int(input("Enter limit: "))
action2 = dls_blocks_world(start_state, goal_state, limit)

# if actions:
#     print("Actions to reach goal state:")
#     for action in actions:
#         print(f"Move block {action[0]} to stack {action[1]}")
# else:
#     print("Goal state cannot be reached from initial state.")