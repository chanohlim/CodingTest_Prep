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

#from utils.print_graph import print_graph

N, M, k = map(int, input().split())

class Shark:

    def __init__(self, n, x, y, d):
        self.n = n
        self.x = x
        self.y = y
        self.d = d

shark_graph = []
smell_graph = [ [ [0,0] for i in range(N) ] for j in range(N)]
sharks = []

# 상 하 좌 우
x_movement = [-1, 1, 0, 0]
y_movement = [0, 0, -1, 1]

shark_priority = [[] for i in range(M)] # shark_priority[0][0] => shark #1 의 윗 방향일때 우선순위 => 불변이므로 따로 클래스로 상태 관리 불필요

for i in range(N):
    shark_graph.append(list(map(int, input().split())))

init_d = list(map(int, input().split()))

for shark in range(1, M+1):

    for x in range(N):
        for y in range(N):
            if shark_graph[x][y] == shark:
                sharks.append(Shark(shark, x, y, init_d[shark-1]))


for i in range(M):
    for j in range(4):
        shark_priority[i].append(list(map(int, input().split())))


def move(N):

    for shark in sharks:

        n, x, y, d = shark.n, shark.x, shark.y, shark.d

        if n == 0: # 퇴출된 상어 무시
            continue

        possible = []
        
        for dir in shark_priority[n-1][d-1]:
            dx, dy = x + x_movement[dir-1], y + y_movement[dir-1]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if smell_graph[dx][dy] != [0, 0]:
                continue

            possible.append((dir, dx, dy))

        if possible: # 만약 갈 수 있는 빈 칸이 존재한다면
            d, dx, dy = possible[0]
            shark_graph[x][y] = 0

            if shark_graph[dx][dy] != 0:
                shark.n = 0 # 퇴출 처리
                continue

            shark_graph[dx][dy] = n
            shark.x, shark.y, shark.d = dx, dy, d


        if not possible: # 만약 갈 수 있는 빈 칸이 존재하지 않는다면

            for dir in shark_priority[n-1][d-1]:
                dx, dy = x + x_movement[dir-1], y + y_movement[dir-1]
    
                if dx < 0 or dx >= N or dy < 0 or dy >= N:
                    continue
    
                if smell_graph[dx][dy][0] == n:
                    break

            shark_graph[x][y] = 0
            shark_graph[dx][dy] = n
            shark.x, shark.y, shark.d = dx, dy, dir

        

    for i in range(N):
        for j in range(N):

            if smell_graph[i][j] != [0, 0]:

                smell_graph[i][j][1] -= 1

                if smell_graph[i][j][1] == 0:
                    smell_graph[i][j] = [0,0]

    for shark in sharks:
            n, x, y, d = shark.n, shark.x, shark.y, shark.d
            if n != 0:
                smell_graph[x][y] = [n, k]
        

#init
for shark in sharks:
    n, x, y, d = shark.n, shark.x, shark.y, shark.d
    smell_graph[x][y] = [n, k]

time = 0


while True:

    if time == 1000:
        time = -2
        break


    move(N)

    alive_cnt = 0

    for shark in sharks:
        n = shark.n
        if n != 0:
            alive_cnt += 1

    if alive_cnt == 1:
        break

    time += 1

print(time + 1)