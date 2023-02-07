class DFS_Traversal:
    # Constructor
    def __init__(self):
        self.graph = dict()

    def addEdge(self, vertex, node):
        self.graph[vertex].append(node)
    
    def DFSUtil(self, vertex, visited):
        visited.add(v)
        print(v, end=' ')

        for i in self.graph[vertex]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self):
        visited = set()

        for i in self.graph:
            if i not in visited:
                self.DFSUtil(i, visited)

if __name__ == "__main__":
    g = DFS_Traversal() # making an object of the class

    n = int(input('Enter number of edges in graph: '))

    for i in range(n):
        vertex = input('vertex :')
        node = input('is connected to: ')
        g.addEdge(vertex, node)

    #calling function
    g.DFS()
    