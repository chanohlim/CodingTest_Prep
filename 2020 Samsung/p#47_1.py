'''

fish를 객체 배열로 만들어서 좌표 관리까지 하는 코드
장점: 매번 맵 탐색(N*N)을 하지 않아도 돼서 N이 커지면 유리하다
단점: 구현이 복잡하고 신경써야될 요소가 많다 -> 실전에선 실수 가능성 UP

7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

33

16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4

43

12 6 14 5 4 5 6 7
15 1 11 7 3 7 7 5
10 3 8 3 16 6 1 1
5 8 2 7 13 6 9 2

76

2 6 10 8 6 7 9 4
1 7 16 6 4 2 5 8
3 7 8 6 7 6 14 8
12 7 15 4 11 3 13 3

39

'''

from sys import stdin
input = stdin.readline

from utils.print_graph import print_graph


class Shark:
    
    def __init__(self, x, y, d, food):
        self.x = x
        self.y = y
        self.d = d
        self.food = food


class Fish:

    def __init__(self, x, y, d, alive):
        self.x = x
        self.y = y
        self.d = d
        self.alive = alive


answer = 0

mx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
my = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def move(fish, shark, graph, N):

    for n in range(1, (N * N) + 1):

        x, y, d, alive = fish[n].x, fish[n].y, fish[n].d, fish[n].alive

        if not alive:
            continue

        switch = False
        for k in range(8):
            dx, dy = x + mx[d], y + my[d]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                d = (d % 8) + 1
                continue

            if dx == shark.x and dy == shark.y:
                d = (d % 8) + 1
                continue

            switch = True
            break

        if switch:
            
            fish[n].d = d
            target = graph[dx][dy]

            if target != 0:
                fish[target].x, fish[target].y = x, y

            fish[n].x, fish[n].y = dx, dy
            graph[dx][dy], graph[x][y] = graph[x][y], graph[dx][dy]



def get_next_prey(shark, graph, N):

    next_prey = []

    x, y, d = shark.x, shark.y, shark.d

    for k in range(N):
        x += mx[d]
        y += my[d]

        if x < 0 or x >= N or y < 0 or y >= N:
            break

        if graph[x][y] != 0:
            next_prey.append((x, y))

    return next_prey


def backtracking(next_prey, shark, fish, graph):
    global answer


    if not next_prey:
        answer = max(answer, shark.food)
        return

    for prey in next_prey:
        dx, dy = prey
        n = graph[dx][dy]

        x, y, d = shark.x, shark.y, shark.d

        shark.x, shark.y, shark.d = dx, dy, fish[n].d
        fish[n].alive = False
        shark.food += n
        graph[dx][dy] = 0

        graph_copy = [row[:] for row in graph]
        fish_copy = [Fish(fish[i].x, fish[i].y, fish[i].d, fish[i].alive) for i in range((N*N) + 1)]

        move(fish_copy, shark, graph_copy, N)
        backtracking(get_next_prey(shark, graph_copy, N), shark, fish_copy, graph_copy)

        shark.x, shark.y, shark.d = x, y, d
        fish[n].alive = True
        shark.food -= n
        graph[dx][dy] = n


N = 4

fish = [Fish(0, 0, 0, False) for i in range( (N * N) + 1)]

graph = []

# fish initialize
for i in range(N):

    data = list(map(int, input().split()))
    graph.append(data[::2])
    for j in range(0, 2*N, 2):
        fish[data[j]].d = data[j + 1]
        fish[data[j]].alive = True

for i in range(N):
    for j in range(N):
        now = graph[i][j]
        fish[now].x, fish[now].y = i, j


init_prey = graph[0][0]

shark = Shark(0, 0, fish[init_prey].d, init_prey)
fish[init_prey].alive = False

graph[0][0] = 0

move(fish, shark, graph, N)

backtracking(get_next_prey(shark, graph, N), shark, fish, graph)

print(answer)