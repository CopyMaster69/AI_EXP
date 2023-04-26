def dfs(graph, start):
    visited = set()
    _dfs(graph, start, visited)
    return visited

def _dfs(graph, node, visited):
    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            _dfs(graph, neighbor, visited)

n = int(input("Enter the number of nodes: "))
graph = {}
for i in range(n):
    node = input("Enter the node: ")
    neighbors = input("Enter the neighbors (separated by spaces): ").split()
    graph[node] = neighbors

start = input("Enter the starting node: ")
visited = dfs(graph, start)
print("\nVisited nodes: ", visited)
