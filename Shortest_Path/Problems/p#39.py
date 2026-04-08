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

T = int(input())

def print_graph(arr):
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()

def mars_1(N):

    INF = int(1e9)

    mars_map = []
    graph = [[] for i in range(N * N)]

    for i in range(N):
        mars_map.append(list(map(int, input().split())))

    distance = [INF] * (N * N)
    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(N):

            index = (i * N) + j

            for k in range(4):
                di, dj = i + movement[k][0], j + movement[k][1]

                if 0 <= di < N and 0 <= dj < N:
                    graph[index].append( ( index + ((di - i) * N + (dj - j)), mars_map[i][j] ) )


    pq = []
    start = 0

    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for node, cost in graph[now]:

            cost += dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(pq, (cost, node))

    print(distance[N*N - 1] + mars_map[N-1][N-1])


def mars_2(N):

    INF = int(1e9)
    
    mars_map = []
    distance = [[INF] * (N) for i in range(N)]
    

    for i in range(N):
        mars_map.append(list(map(int, input().split())))
    
    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    pq = []

    heapq.heappush(pq, (mars_map[0][0], (0,0))) # cost, (i, j)
    distance[0][0] = mars_map[0][0]

    while pq:

        dist, coor = heapq.heappop(pq)
        i, j = coor

        if dist > distance[i][j]: # 어차피 더 작을 수가 없으니 스킵 => 오래된 데이터이다, 이미 최단거리가 확정된 노드임(pop된 순간 최단거리로 확정)
            continue

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            cost = dist + mars_map[di][dj]

            if cost < distance[di][dj]:
                distance[di][dj] = cost
                heapq.heappush(pq, (cost, (di, dj)))

    print(distance[N-1][N-1])

            

for i in range(T):
    n = int(input())
    mars_2(n)