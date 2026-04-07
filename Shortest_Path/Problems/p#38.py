'''

6 6
1 5
3 4
4 2
4 6
5 2
5 4

'''

import heapq

INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
distance_table = [[INF] * (N + 1) for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def djikstra(start):
    
    pq = []
    heapq.heappush(pq, start)

    distance_table[start][start] = 0

    while pq:
        now = heapq.heappop(pq)

        for node in graph[now]:
            distance_table[start][node] = min(distance_table[start][node], distance_table[start][now] + 1)
            heapq.heappush(pq, node)

    return distance_table

for i in range(1, N+1):
    djikstra(i)

cnt = 0

for i in range(1, N+1):
    flag = [False] * (N + 1)

    for j in range(1, N+1):
        
        if distance_table[i][j] != INF:
            flag[j] = True

        if distance_table[j][i] != INF:
            flag[j] = True

    if all(flag[1:]) == True:
        cnt += 1

print(cnt)

        
