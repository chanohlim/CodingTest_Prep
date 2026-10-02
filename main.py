'''

5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

14

4 2 6
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
4 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3

26

5 4 1
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

-1

5 4 10
0 0 0 0 3
0 0 0 0 0
1 2 0 0 0
0 0 0 0 4
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

-1

'''
from utils.print_graph import print_graph
from sys import stdin
input = stdin.readline


N, M, k = map(int, input().split())

class Shark:

    def __init__(self, n, x, y, d, alive):
        self.n = n
        self.x = x
        self.y = y
        self.d = d
        self.alive = alive

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]


n_shark = M


def move(graph, scent_map, sharks, preference, N, M, k):
    global n_shark

    for shark in sharks:
        
        n, x, y, d, alive = shark.n, shark.x, shark.y, shark.d, shark.alive

        if not alive:
            continue

        possible = False
        for p in preference[n-1][d-1]:

            dx, dy = x + mx[p-1], y + my[p-1]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if scent_map[dx][dy] != [0, 0]:
                continue

            possible = True
            break


        if not possible: # 인접한 냄새가 없는 칸이 없음

            for p in preference[n-1][d-1]:

                dx, dy = x + mx[p-1], y + my[p-1]

                if dx < 0 or dx >= N or dy < 0 or dy >= N:
                    continue

                if scent_map[dx][dy][0] == n:
                    break

        if graph[dx][dy] != 0:
            shark.alive = False
            n_shark -= 1
            graph[x][y] = 0

        else:
            shark.x, shark.y, shark.d = dx, dy, p
            graph[dx][dy] = n
            graph[x][y] = 0


    for i in range(N):
        for j in range(N):
            if scent_map[i][j][0] != 0:
                scent_map[i][j][1] -= 1
                if scent_map[i][j][1] == 0:
                    scent_map[i][j] = [0, 0]

    for shark in sharks:
        if shark.alive == False:
            continue
        
        n, x, y = shark.n, shark.x, shark.y
        scent_map[x][y] = [n, k]

            

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

sharks = [ Shark(i+1, 0, 0, 0, False) for i in range(M) ]
scent_map = [ [[0,0] for i in range(N)] for j in range(N) ]

init_d = list(map(int, input().split()))

for i in range(M):
    sharks[i].d = init_d[i]
    sharks[i].alive = True

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            sharks[graph[i][j] - 1].x, sharks[graph[i][j] - 1].y = i, j
            scent_map[i][j] = [graph[i][j], k]

print_graph(scent_map)


preference = [ [] for i in range(M) ]
for i in range(M):
    for j in range(4):
        preference[i].append(list(map(int, input().split())))


time = 0

while n_shark > 1:

    move(graph, scent_map, sharks, preference, N, M, k)
    print_graph(scent_map)
    time += 1

    if time > 1000:
        time = -1
        break

print(time)