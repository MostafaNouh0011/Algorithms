graph = {'A':['B', 'C'], 
         'B':['D', 'E', 'F'], 
         'C':['G'], 
         'D':[], 
         'E':[], 
         'F':['H'], 
         'G':['I'], 
         'H':[], 
         'I':[]}


def BFS(graph, start_node):
    visited = []
    queue = []

    queue.append(start_node)
    visited.append(start_node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


if __name__ == "__main__":
    BFS(graph, 'A')