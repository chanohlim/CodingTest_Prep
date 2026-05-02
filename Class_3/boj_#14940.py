'''

15 15
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 2 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 0 1

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34

'''
from sys import stdin
input = stdin.readline
from collections import deque

movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j, N, M):

    distance = [[-1] * M for k in range(N)]

    q = deque()
    q.append((i, j))
    distance[i][j] = 0

    while q:
        i, j = q.popleft()

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 0:
                continue

            if graph[di][dj] == 1 and distance[di][dj] == -1: # 방문 가능하고 아직 방문하지 않았으면
                distance[di][dj] = distance[i][j] + 1
                q.append((di, dj))

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(0, end = ' ')
                continue

            print(distance[i][j], end = ' ')
        print()
        



N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))


found = False

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            bfs(i, j, N, M)
            found = True
            break
        
    if found:
        break