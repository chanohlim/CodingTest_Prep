'''

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

4

'''

from collections import deque
from sys import stdin

input = stdin.readline

M, N, H = map(int, input().split())
move = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)] # 앞 뒤 상 하 좌 우 -> 3차원 배열

def bfs(tomato):

    q = deque(tomato)
    day = -1


    while q:
        i, j, k, day = q.popleft()
        
        for l in range(6):
            di, dj, dk = i + move[l][0], j + move[l][1], k + move[l][2]

            if (di >= H) or (di < 0) or (dj >= N) or (dj < 0) or (dk >= M) or (dk < 0):
                continue

            if graph[di][dj][dk] == 0:
                graph[di][dj][dk] = 1
                q.append((di, dj, dk, day + 1))

    return day




graph = []
tomato = []

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))

    graph.append(temp)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                tomato.append((i, j, k, 0))

answer = bfs(tomato)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                answer = -1
                break

print(answer)