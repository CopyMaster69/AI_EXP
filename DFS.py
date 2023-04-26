def dfs(graph, start):
    visited = set()
    _dfs(graph, start, visited)
    return visited

def _dfs(graph, node, visited):
    visited.add(node)
    print(node, end=' ')

    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and neighbor not in visited:
            _dfs(graph, neighbor, visited)

n = int(input("Enter the number of nodes: "))
print("Enter the adjacency matrix: ")
matrix = [list(map(int, input().split())) for i in range(n)]
start = int(input("Enter the starting node: "))
visited = dfs(matrix, start)
print("\nVisited nodes: ", visited)
