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
from collections import deque

INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
distance_table = [[INF] * (N + 1) for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):

    q = deque()
    q.append(start)

    distance_table[start][start] = 0

    while q:
        now = q.popleft()
        
        for node in graph[now]:
            if distance_table[start][node] == INF:
                distance_table[start][node] = distance_table[start][now] + 1
                q.append(node)


def floyd(N):

    for i in range(1, N+1):
        for j in graph[i]:
            distance_table[i][j] = 1

    for i in range(1, N+1):
        distance_table[i][i] = 0

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance_table[i][j] = min(distance_table[i][j],
                                           distance_table[i][k] + distance_table[k][j])



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
    bfs(i)

floyd(N)

for i in distance_table:
    for j in i:
        if j == INF:
            print('X', end = ' ')
        else:
            print(j, end = ' ')
    print()

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
        print(i)

print(cnt)

        
