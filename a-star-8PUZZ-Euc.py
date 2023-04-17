import math
import heapq

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_heuristic(state):
    goal = [[0, 1, 2], [7, 8, 3], [6, 5, 4]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                current_pos = (i, j)
                goal_pos = get_position_in_goal_state(state[i][j], goal)
                distance += math.sqrt((goal_pos[0]-current_pos[0])**2 + (goal_pos[1]-current_pos[1])**2)
    return distance

def get_position_in_goal_state(value, goal):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == value:
                return i, j

def get_children(state):
    children = []
    blank_pos = get_blank_position(state)
    if blank_pos[0] > 0:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]], new_state[blank_pos[0]-1][blank_pos[1]] = new_state[blank_pos[0]-1][blank_pos[1]], new_state[blank_pos[0]][blank_pos[1]]
        children.append(new_state)
    if blank_pos[0] < 2:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]], new_state[blank_pos[0]+1][blank_pos[1]] = new_state[blank_pos[0]+1][blank_pos[1]], new_state[blank_pos[0]][blank_pos[1]]
        children.append(new_state)
    if blank_pos[1] > 0:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]], new_state[blank_pos[0]][blank_pos[1]-1] = new_state[blank_pos[0]][blank_pos[1]-1], new_state[blank_pos[0]][blank_pos[1]]
        children.append(new_state)
    if blank_pos[1] < 2:
        new_state = [list(row) for row in state]
        new_state[blank_pos[0]][blank_pos[1]], new_state[blank_pos[0]][blank_pos[1]+1] = new_state[blank_pos[0]][blank_pos[1]+1], new_state[blank_pos[0]][blank_pos[1]]
        children.append(new_state)
    return children

def a_star_search(start_state, goal_state):
    visited = set()
    queue = []
    heapq.heappush(queue, (get_heuristic(start_state), start_state))
    while queue:
        current_state = heapq.heappop(queue)[1]
        visited.add(str(current_state))
        print(current_state)
        if current_state == goal_state:
            return current_state
        for child in get_children(current_state):
            if str(child) not in visited:
                heapq.heappush(queue, (get_heuristic(child), child))

start = [[1,2,3], [8, 0, 4], [7,6,5]]
goal = [[0,1,2], [7,8,3],[6,5,4]]

a_star_search(start, goal)