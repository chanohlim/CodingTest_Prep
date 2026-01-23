# 미래 도시 코드를 플로이드-워셜로도 구현


import sys

INF = int(1e9)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(N):
    graph[i+1][i+1] = 0

X, K = map(int, input().split())

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][K] + graph[K][X]

print(graph)

if distance >= INF:
    print('-1')
else:
    print(distance)