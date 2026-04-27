'''

2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

5
1

'''
from sys import stdin
input = stdin.readline

from collections import deque

movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j, M, N):

    q = deque()
    q.append((i, j))

    while q:
        i, j = q.popleft()

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 1:
                graph[di][dj] = 0
                q.append((di, dj))

T = int(input())

for t in range(T):
    cnt = 0

    M, N, K = map(int, input().split())
    
    graph = [[0] * M for i in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j, M, N)
                cnt += 1

    print(cnt)
