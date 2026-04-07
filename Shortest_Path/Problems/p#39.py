from collections import deque

T = int(input())

def mars(N):

    q = deque()
    
    graph = []

    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

    for i in range(N):
        graph.append(list(map(int, input().split())))

    q.append((0,0))

    while q:
        i, j = q.popleft
        graph[i][j] = -1 # 방문 표시

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue
            
            if graph[di][dj] != -1:
                graph[di][dj] += graph[i][j]
                continue


            graph[di][dj] = min(
                graph[di][dj],
                graph[i][j] + )





for i in range(T):
    n = int(input())
    mars(n)