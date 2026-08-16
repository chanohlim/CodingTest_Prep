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

import heapq as h
from print_graph import print_graph

INF = int(1e9)

T = int(input())

movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def Dijkstra(N):

    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * N for i in range(N)]
    
    pq = []
    h.heappush(pq, (graph[0][0], (0,0))) # cost, 좌표
    distance[0][0] = graph[0][0]

    while pq:
        dist, now = h.heappop(pq)
        i, j = now

        if dist > distance[i][j]: # 현재 꺼낸 경로가 이미 더 짧은 최단경로로 갱신이 된 경우 => 굳이 안봐도 됨
            continue

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            cost = dist + graph[di][dj]

            if cost < distance[di][dj]: # 더 좋은 경로를 발견하면 해당 노드까지의 최단거리를 갱신하고, 새로운 정보를 다시 탐색한다.
                distance[di][dj] = cost
                h.heappush(pq, (cost, (di, dj)))

    print_graph(distance)
    print(distance[N-1][N-1])

for t in range(T):

    N = int(input())
    Dijkstra(N)