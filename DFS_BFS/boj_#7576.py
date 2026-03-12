'''

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8

'''

from collections import deque
from sys import stdin

input = stdin.readline

M, N = map(int, input().split())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(tomato):

    q = deque(tomato)
    day = -1


    while q:
        i, j, day = q.popleft()
        
        for k in range(4):
            di, dj = i + move[k][0], j + move[k][1]

            if (di >= N) or (di < 0) or (dj >= M) or (dj < 0):
                continue

            if graph[di][dj] == 0:
                graph[di][dj] = 1
                q.append((di, dj, day + 1))
            else:
                continue

    return day




graph = []
tomato = []

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i, j, 0))

answer = bfs(tomato)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer = -1
            break

print(answer)
