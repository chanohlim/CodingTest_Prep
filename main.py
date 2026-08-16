'''

6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

'''

from sys import stdin
from utils.print_graph import print_graph
from collections import deque

input = stdin.readline
N, M = map(int, input().split())

INF = int(1e9)
distance = [INF] * (N + 1)
visited = [False] * (N + 1)

graph = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(start):

    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()

        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                distance[node] = distance[now] + 1
                q.append(node)

    max_dist = max(distance[1:])
    candidates = [i for i in range(1, N+1) if distance[i] == max_dist]

    print(candidates[0], max_dist, len(candidates))

BFS(1)