'''

3
0 0 0
0 0 0
0 9 0

0

3
0 0 1
0 0 0
0 9 0

3

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

14

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6

60

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

48

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9

39

'''

from sys import stdin
input = stdin.readline

from utils.print_graph import print_graph

from collections import deque

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            now = (i, j)

size = 2
eat_cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start, visited, size, N):

    q = deque()

    i, j = start
    distance = 0

    q.append((distance, i, j))
    visited[i][j] = True

    possible = []
    

    while q:
        distance, i, j = q.popleft()

        for k in range(4):
            di, dj = i + dx[k], j + dy[k]

            if di >= N or di < 0 or dj >= N or dj < 0:
                continue

            if visited[di][dj]: # 상어 자신이 있었던 칸이면 skip
                continue

            if graph[di][dj] == 0: # 빈칸일 때
                visited[di][dj] = True # 방문 처리
                q.append((distance + 1, di, dj))
            elif 1 <= graph[di][dj] <= 6: # 다른 물고기가 있을 때
                if graph[di][dj] > size: # 만약 자신보다 크기가 크면 skip
                    continue
                elif graph[di][dj] == size: # 같으면 지나갈 수 있음
                    visited[di][dj] = True
                    q.append((distance + 1, di, dj))
                else: # 자신보다 작으면
                    possible.append((distance + 1, di,dj)) # 먹을 수 있는 후보로 추가


    return possible


visited = [[False] * N for i in range(N)]
possible = bfs(now, visited, size, N)

time = 0

while possible:
    possible.sort(key=lambda x: (x[0], x[1], x[2]))

    prev_i, prev_j = now
    distance, i, j = possible[0]

    eat_cnt += 1
    if eat_cnt == size:
        size += 1
        eat_cnt = 0

    
    graph[i][j] = 9
    now = (i, j)
    graph[prev_i][prev_j] = 0

    time += distance

    visited = [[False] * N for i in range(N)]

    possible = bfs(now, visited, size, N)


print(time)