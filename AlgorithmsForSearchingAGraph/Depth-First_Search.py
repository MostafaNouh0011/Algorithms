from collections import deque

graph = {'A':['G', 'B'], 
         'B':['E', 'D', 'C'], 
         'C':[], 
         'D':[], 
         'E':['F'], 
         'F':[], 
         'G':['H'], 
         'H':['I'], 
         'I':[]}

def DFS(graph, start_node):
    visited = []
    stack = deque()

    stack.append(start_node)
    visited.append(start_node)

    while stack:
        s = stack.pop()
        print(s, end=' ')

        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                stack.append(i)


if __name__ == "__main__":
    DFS(graph, 'A')
