def tower_of_hanoi_dls(start, goal, depth):
    stack = [(start, [], 0)]

    while stack:
        state, moves, level = stack.pop()

        print(f"Level {level}: {state}")

        if state == goal:
            return moves

        if len(moves) >= depth:
            continue

        for i in range(3):
            if state[i]:
                for j in range(3):
                    if i != j and (not state[j] or state[j][-1] > state[i][-1]):
                        new_state = [list(tower) for tower in state]
                        new_state[j].append(new_state[i].pop())

                        stack.append((new_state, moves + [(i, j)], level + 1))

    return None


def main():
    start = [[2], [1,3], []]
    goal = [[], [], [1,2,3]]
    depth = 1

    moves = tower_of_hanoi_dls(start, goal, depth)

    if moves:
        print("Solution found in, ", str(len(moves)), " moves: ", moves)
    else:
        print("No solution found within depth limit.")


if __name__ == '__main__':
    main()