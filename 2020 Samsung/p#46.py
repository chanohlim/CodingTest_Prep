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
from collections import deque
from copy import deepcopy
from sys import stdin
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

def find_target(ocean, start, size, fish_cnt, time):

    q = deque()
    prey = []
    min_dist = N*N
    q.append(start)

    while q:

        i, j = q.popleft()    

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di >= N or di < 0 or dj >= N or dj < 0:
                continue

            if ocean[di][dj] == 0 or ocean[di][dj] == size: # 지나갈 수 있는 경로이면
                ocean[di][dj] = ocean[i][j] + 10
                q.append((di, dj))

            elif 0 < ocean[di][dj] < size: # 먹을 수 있는 물고기이면
                dist = ocean[i][j]//10 + 1

                if dist == min_dist:
                    prey.append((di, dj, dist)) # 좌표와 거리
                elif dist < min_dist:
                    min_dist = dist
                    prey = [(di, dj, dist)]
            else:
                continue

    if len(prey) != 0:
        prey.sort(key=lambda x: (x[0], x[1]))
        fish_cnt += 1
        time += prey[0][2]
        return (prey[0][0], prey[0][1], fish_cnt, time)


    return (False, False, fish_cnt, time)
            

for i in range(N*N):

    

    ocean = deepcopy(graph)
    graph[start[0]][start[1]] = 0

    x, y, fish_cnt, time = find_target(ocean, start, size, fish_cnt, time)

    if fish_cnt == size:
        if size < 7:
            size += 1
            fish_cnt = 0

    if x is False:
        break
    
    graph[x][y] = 9
    start = (x, y)

print(time)