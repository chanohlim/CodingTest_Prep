from collections import deque


def BFS(graph, visited, start):

    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end = ' ')
        
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

    

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

BFS(graph, visited, 1)