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

visited[][]행렬으로 방문 처리 + 거리 처리 한번에.
ocean으로 현 맵을 복사해서 복잡하게 하기보단, 매번 bfs를 호출할 때마다 visited 행렬을 초기화

bfs에서 큐에 들어갔다가 나오는 노드들은 오름차순이다. 따라서 min_dist 보다 거리가 먼 노드가 나오기 시작하면 그 다음부터는 보지 않아도 됨.

min_dist로 bfs 레벨 관리: 레벨이 깊어질 수록 거리가 멀어지니까 min_dist 이상이 나오면 바로 break

'''
from collections import deque
from sys import stdin
from time import sleep
import os
input = stdin.readline


N = int(input())
graph = []
fish_cnt = 0
time = 0
size = 2

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            start = (i,j)


movement = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위 아래 좌 우

def print_graph(arr):
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()

def find_target(start, size, fish_cnt, time):

    visited = [[-1] * N for i in range(N)]
    q = deque()
    prey = []
    min_dist = N * N
    q.append(start)
    visited[start[0]][start[1]] = 0


    while q:

        i, j = q.popleft()

        if visited[i][j] > min_dist: # 같은 레벨에 있는 먹이들 전부 탐색 완료했으니 break
            break

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di >= N or di < 0 or dj >= N or dj < 0:
                continue

            if visited[di][dj] != -1: # 이미 방문한 노드면
                continue

            if graph[di][dj] > size: # 먹을 수 없는 크기의 물고기면
                continue

            if 0 < graph[di][dj] < size: # 먹을 수 있는 크기의 물고기면
                
                if visited[i][j] + 1 == min_dist:
                    prey.append((di, dj, min_dist))
                elif visited[i][j] + 1 < min_dist:
                    min_dist = visited[i][j] + 1
                    prey = [(di, dj, min_dist)]


                visited[di][dj] = visited[i][j] + 1

            elif graph[di][dj] == size or graph[di][dj] == 0: # 방문하지 않은 노드이면 (크기가 같은 물고기이면)
                visited[di][dj] = visited[i][j] + 1
                q.append((di, dj))
            


    if len(prey) != 0:
        prey.sort(key=lambda x: (x[0], x[1]))
        fish_cnt += 1
        time += prey[0][2]
        return (prey[0][0], prey[0][1], fish_cnt, time)


    return (False, False, fish_cnt, time)
            

for i in range(N*N):
    
    # print_graph(graph)

    x, y, fish_cnt, time = find_target(start, size, fish_cnt, time)

    if fish_cnt == size:
        if size < 7:
            size += 1
            fish_cnt = 0

    if x is False:
        break
    
    graph[start[0]][start[1]] = 0
    graph[x][y] = 9

    start = (x, y)
    # sleep(0.3)
    # os.system('clear')

print(time)