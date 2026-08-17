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

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]


def Dijkstra(N):

    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * N for i in range(N)]


    pq = []
    heapq.heappush(pq, (graph[0][0], (0, 0)))
    distance[0][0] = graph[0][0]

    while pq:
        dist, now = heapq.heappop(pq)
        i, j = now

        if dist > distance[i][j]:
            continue

        for k in range(4):
            di, dj = i + dx[k], j + dy[k]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            cost = dist + graph[di][dj]
            if cost < distance[di][dj]:
                distance[di][dj] = cost
                heapq.heappush(pq, (cost, (di, dj)))

    print(distance[N-1][N-1])






T = int(input())

for t in range(T):
    N = int(input())
    Dijkstra(N)