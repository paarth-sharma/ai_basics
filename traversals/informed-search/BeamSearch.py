from numpy import array
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

 
#beta here is width of beam and distances can be considered as weights.
def beam_search(distances, beta):
    #initialising some record
    paths_so_far = [[list(), 0]]  
  
    #traverse through the neighbouring vertices row by row.
    for idx, tier in enumerate(distances):
        if idx > 0:
            print(f'Paths kept after tier {idx-1}:')
            print(*paths_so_far, sep='\n')
        paths_at_tier = list()
         
 
        for i in range(len(paths_so_far)):
            path, distance = paths_so_far[i]
             
            # Extending the paths
            for j in range(len(tier)):
                path_extended = [path + [j], distance + tier[j]]
                paths_at_tier.append(path_extended)
                 
        paths_ordered = sorted(paths_at_tier, key=lambda element: element[1])
         
        # The best paths are saved
        paths_so_far = paths_ordered[:beta]
        print(f'\nPaths pruned after tier {idx}: ')
        print(*paths_ordered[beta:], sep='\n')
         
    return paths_so_far
 

# 1st row ---> [0->0 distance ,0->1 distance, 0->2 distance, 0->3 distance]
# and so on
# 0 means node itself, if on DIAGONAL of matrix, else not connect to each other
dists = array([[0, 10, 15, 20],
               [10, 0, 35, 25],
               [15, 35, 0, 30],
               [20, 25, 30, 0]])
 
# Calculating the best paths
best_paths = beam_search(dists, 2)
print('\nThe best paths:')
for beta_path in best_paths:
    print(beta_path)

""" (OPTIONAL) visualising the graph in the distance matrix """

# create a graph object
G = nx.Graph()

# create a list of nodes
num_nodes = dists.shape[0]
nodes = range(num_nodes)

# add nodes to the graph
G.add_nodes_from(nodes)

# add edges to the graph
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        weight = dists[i][j]
        if weight > 0:
            G.add_edge(i, j, weight=weight)

# draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): dists[i][j] for i in nodes for j in G.neighbors(i)})

plt.show()

