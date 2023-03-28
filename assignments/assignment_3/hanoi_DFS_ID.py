def hanoi_iterative_deepening(start, end):
    n = len(start[0])
    stack = [(1, start, end)]
    depth = 0
    
    while stack:
        cur_depth, cur_start, cur_end = stack.pop()
        if cur_depth > depth:
            depth = cur_depth
            print("Depth: ", depth)
            print("------------")
            print_state(cur_start, cur_end)
        if cur_start[0] == [] and cur_start[1] == [] and cur_depth <= n:
            disk = cur_end[2].pop()
            cur_start[2].append(disk)
            print(f"Move disk {disk} from peg {end.index(cur_end)+1} to peg {start.index(cur_start)+1}")
        elif cur_depth <= n:
            for i in range(3):
                for j in range(3):
                    if i != j and cur_start[i] != []:
                        if cur_end[j] == [] or cur_start[i][-1] < cur_end[j][-1]:
                            new_start = [cur_start[k][:] for k in range(3)]
                            new_end = [cur_end[k][:] for k in range(3)]
                            disk = new_start[i].pop()
                            new_end[j].append(disk)
                            stack.append((cur_depth+1, new_start, new_end))

    return depth

def print_state(start, end):
    for i in range(max(len(start[0]), len(start[1]), len(start[2]))-1, -1, -1):
        for peg in [start, end]:
            if i < len(peg[0]):
                print(peg[0][i], end='\t')
            else:
                print('-', end='\t')

            if i < len(peg[1]):
                print(peg[1][i], end='\t')
            else:
                print('-', end='\t')
                
            if i < len(peg[2]):
                print(peg[2][i], end='\t')
            else:
                print('-', end='\t')
        print()

def main():
    n = 4
    start = [[3], [1,2], []]
    end = [[], [], [3,2,1]]
    depth = hanoi_iterative_deepening(start, end)
    print("Solution found at depth: ", depth)

if __name__ == '__main__':
    main()