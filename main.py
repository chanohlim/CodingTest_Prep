'''

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
from copy import deepcopy

direction_x = [0, -1, -1, 0, 1, 1, 1, 0, -1]
direction_y = [0, 0, -1, -1, -1, 0, 1, 1, 1]

fish_d = [0] * 17

result = 0

class Shark:

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d


graph = [[] for i in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        n = data[2*j] # 물고기의 번호
        graph[i].append(n)
        fish_d[n] = data[2*j + 1]


def movement(shark, graph, fish_d):

    shark_x, shark_y = shark.x, shark.y

    for fish in range(1, 17):

        if fish_d[fish] == 0: # 죽은 물고기는 패스
            continue

        for i in range(4):
            for j in range(4):
                if graph[i][j] == fish:
                    x, y = i, j
                    break

        d = fish_d[fish]

        for i in range(8):

            dx, dy = x + direction_x[d], y + direction_y[d]

            if (dx < 0 or dx >= 4 or dy < 0 or dy >= 4) or (shark_x == dx and shark_y == dy):
                d = (d % 8) + 1
                continue

            possible = True
            break

        if possible:
            fish_d[fish] = d
            graph[dx][dy], graph[x][y] = graph[x][y], graph[dx][dy]


def possible_prey(shark, graph):

    x, y, d = shark.x, shark.y, shark.d
    possible = []

    for i in range(1, 4):
        dx, dy = x + direction_x[d]*i, y + direction_y[d]*i

        if (dx < 0 or dx >= 4 or dy < 0 or dy >= 4) or (graph[dx][dy] == 0):
            continue

        possible.append((dx, dy))

    return possible


def hunt(shark, prey, graph, fish_d): # 상어가 물고기가 있는 좌표로 이동 후 물고기를 먹기

    x, y = shark.x, shark.y
    dx, dy = prey
    fish = graph[dx][dy]

    shark.d = fish_d[fish]
    shark.x, shark.y = dx, dy

    graph[dx][dy] = 0
    fish_d[fish] = 0 # 죽음 처리

    return fish


def backtracking(shark, total, graph, fish_d):

    global result

    possible = possible_prey(shark, graph)

    if not possible:
        result = max(result, total)
        return

    for p in possible:

        graph_copy = deepcopy(graph)
        fish_d_copy = deepcopy(fish_d)

        x, y, d = shark.x, shark.y, shark.d

        prey = hunt(shark, p, graph_copy, fish_d_copy)
        movement(shark, graph_copy, fish_d_copy)

        backtracking(shark, total + prey, graph_copy, fish_d_copy)

        shark.x, shark.y, shark.d = x, y, d




#init
init_prey = graph[0][0]

shark = Shark(0, 0, fish_d[init_prey])
fish_d[init_prey] = 0 # 죽음 처리

graph[0][0] = 0 # 빈 칸으로 처리


movement(shark, graph, fish_d)

backtracking(shark, init_prey, graph, fish_d)

print(result)