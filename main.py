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

from sys import stdin
input = stdin.readline

from utils.print_graph import print_graph

N, M, k = map(int, input().split())

# 위(1) 아래(2) 왼쪽(3) 오른쪽(4)
movement_x = [0, -1, 1, 0, 0]
movement_y = [0, 0, 0, -1, 1]

sharks = []
shark_graph = []
scent_graph = [[ [0,0] for i in range(N) ] for i in range(N)]


priority = [[] for i in range(M)] # priority[a-1][b-1] => a 상어가 b 방향으로 갈 때의 우선순위

class Shark:

    def __init__(self, n, x, y, d):
        self.n = n
        self.x = x
        self.y = y
        self.d = d

sharks.append(Shark(0, 0, 0, 0)) # dummy shark

for i in range(N):
    shark_graph.append(list(map(int, input().split())))


init_d = list(map(int, input().split()))

for n in range(1, M+1):
    d = init_d[n-1]
    for i in range(N):
        for j in range(N):
            if shark_graph[i][j] == n:
                sharks.append(Shark(n, i, j, d))

for i in range(M):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))



for shark in sharks:
    n, x, y = shark.n, shark.x, shark.y

    if n == 0:
        continue

    scent_graph[x][y] = [n, k]


def movement(N, sharks, k):

    for shark in sharks:

        n, x, y, d = shark.n, shark.x, shark.y, shark.d

        if n == 0: # 퇴출된 상어는 무시
            continue

        possible = False

        for dir in priority[n-1][d-1]:
            dx, dy = x + movement_x[dir], y + movement_y[dir]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if scent_graph[dx][dy] != [0, 0]:
                continue

            possible = True
            shark.d = dir
            break

        if possible:

            if shark_graph[dx][dy] != 0:
                shark.n = 0 # 퇴출 처리
                shark_graph[x][y] = 0
        
            else:
                shark_graph[dx][dy] = n
                shark_graph[x][y] = 0
                shark.x, shark.y = dx, dy

        else:

            for dir in priority[n-1][d-1]:
                dx, dy = x + movement_x[dir], y + movement_y[dir]

                if dx < 0 or dx >= N or dy < 0 or dy >= N:
                    continue

                if scent_graph[dx][dy][0] == n:
                    shark_graph[dx][dy] = n
                    shark_graph[x][y] = 0
                    shark.x, shark.y , shark.d = dx, dy, dir
                    break


    for i in range(N):
        for j in range(N):
            if scent_graph[i][j][0] != 0:
                scent_graph[i][j][1] -= 1
                if scent_graph[i][j][1] == 0:
                    scent_graph[i][j] = [0, 0]
                        
    for shark in sharks:

        n, x, y = shark.n, shark.x, shark.y

        if n == 0:
            continue

        scent_graph[x][y] = [n, k]



time = 0

while True:

    alive = 0

    for shark in sharks:
        n = shark.n

        if n != 0:
            alive += 1

    if alive == 1:
        break

    if time == 1000:
        time = -1
        break

    movement(N, sharks, k)

    time += 1

print(time)