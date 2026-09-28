'''

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

20
19
36

'''

import heapq
from utils.print_graph import print_graph
from sys import stdin
input = stdin.readline

INF = int(1e9)


def Dijkstra(N, graph):

    distance = [[INF] * N for i in range(N)]
    visited = [[False] * N for i in range(N)]

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]

    distance[0][0] = graph[0][0]

    pq = []
    heapq.heappush(pq, (distance[0][0], (0, 0)))
    visited[0][0] = True

    while pq:

        dist, now = heapq.heappop(pq)
        x, y = now

        if dist > distance[x][y]:
            continue

        for k in range(4):
            dx, dy = x + mx[k], y + my[k]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if visited[dx][dy]:
                continue

            cost = dist + graph[dx][dy]
            if cost < distance[dx][dy]:
                heapq.heappush(pq, (cost, (dx, dy)))
                visited[dx][dy] = True
                distance[dx][dy] = cost

    return distance[N-1][N-1]
    
            


T = int(input())
answer = []

for t in range(T):
    
    N = int(input())
    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))

    answer.append(Dijkstra(N, graph))

for a in answer:
    print(a)
