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

from copy import deepcopy


graph = [[] for i in range(4)]
fish_direction = [0] * 17

result = 0

direction = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish = data[2*j]
        fish_direction[fish] = data[2*j + 1]
        graph[i].append(fish)


class Shark:

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d



def movement(shark, graph, fish_direction):

    shark_x, shark_y = shark.x, shark.y

    for fish in range(1, 17):

        d = fish_direction[fish]

        if d == 0:
            continue

        for i in range(4):
            for j in range(4):
                if graph[i][j] == fish:
                    x, y = i, j
                    break


        possible = False

        for i in range(8):
            dx, dy = x + direction[d][0], y + direction[d][1]
            
            if (dx < 0 or dx >= 4 or dy < 0 or dy >= 4) or (dx == shark_x and dy == shark_y):
                d = d % 8 + 1
                continue

            possible = True
            break

        if possible:
            fish_direction[fish] = d
            graph[dx][dy], graph[x][y] = graph[x][y], graph[dx][dy]

def possible_prey(shark, graph):

    x, y, d = shark.x, shark.y, shark.d
    possible = []

    for i in range(1, 4):
        dx, dy = x + (direction[d][0] * i), y + (direction[d][1] * i)

        if (dx < 0 or dx >= 4 or dy < 0 or dy >= 4) or (graph[dx][dy] == 0):
            continue

        possible.append((dx, dy))

    return possible


def hunt(shark, prey_coor, graph, fish_direction):

    dx, dy = prey_coor

    prey = graph[dx][dy]

    shark.d = fish_direction[prey] # 상어가 물고기의 방향 습득
    fish_direction[prey] = 0 # 물고기 죽음

    graph[dx][dy] = 0 # 빈 칸 처리
    shark.x, shark.y = dx, dy # 상어의 위치 업데이트


def backtracking(shark, size, graph, fish_direction):
    global result

    possible = possible_prey(shark, graph)

    if not possible:
        result = max(result, size)
        return

    for p in possible:

        shark_x, shark_y, shark_d = shark.x, shark.y, shark.d
        prey = graph[p[0]][p[1]]

        graph_copy = deepcopy(graph)
        fish_d_copy = deepcopy(fish_direction)

        hunt(shark, p, graph_copy, fish_d_copy)

        movement(shark, graph_copy, fish_d_copy)

        backtracking(shark, size + prey, graph_copy, fish_d_copy)

        shark.x, shark.y, shark.d = shark_x, shark_y, shark_d







#init
init_prey = graph[0][0]
shark = Shark(0, 0, fish_direction[init_prey])
graph[0][0] = 0
fish_direction[init_prey] = 0

movement(shark, graph, fish_direction)

backtracking(shark, init_prey, graph, fish_direction)

print(result)
