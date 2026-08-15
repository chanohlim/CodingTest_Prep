'''

6 6
1 5
3 4
4 2
4 6
5 2
5 4

'''

from sys import stdin
from utils.print_graph import print_graph

input = stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0

for n in range(1, N+1):
    possible = True
    for i in range(1, N+1):
        if min(graph[n][i], graph[i][n]) == INF:
            possible = False

    if possible:
        cnt += 1


print(cnt)