
def DFS(graph, start, visited):

    print(start, end = ' ')
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            DFS(graph, node, visited)


graph = [
    [],
    [2, 3, 8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

DFS(graph, 1, visited)
