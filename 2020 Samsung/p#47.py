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

graph = [[] for i in range(4)]
directions = [0] * (17) # 1:북 - 2:북서 - 3:서 - 4:남서 - 5:남 - 6:남동 - 7:동 - 8:북동

movement = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

result = 0

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        graph[i].append(temp[j])
        directions[temp[j]] = temp[j + 1]


def print_graph(arr):
    for i in arr:
        for j in i:
            print("%2d" % j, end = ' ')
        print()

def rotate(fish, directions):

    if directions[fish] == 8:
        directions[fish] = 1
    else:
        directions[fish] += 1


def moveable(fish, i, j, directions, graph):

    di, dj = i + movement[directions[fish]][0], j + movement[directions[fish]][1]

    if di < 0 or di >= 4 or dj < 0 or dj >= 4: # 이동하려는 칸이 공간의 경계를 넘는 칸이면
        return False
    
    if graph[di][dj] == 0: # 이동하려는 칸에 상어가 있으면
        return False

    return True

def find_prey(i, j, directions, graph):

    prey = []
    shark_direction = directions[0]

    x = 1


    di, dj = i + movement[shark_direction][0] * x, j + movement[shark_direction][1] * x
    
    while 0 <= di < 4 and 0 <= dj < 4:

        
        if graph[di][dj] != -1:
            prey.append(graph[di][dj])
        
        x += 1
        di, dj = i + movement[shark_direction][0] * x, j + movement[shark_direction][1] * x
        

    return prey

def fish_move(directions, graph):
    for fish in range(1, 17):

        move = True
        
        if directions[fish] == 0: # 이미 먹혔으면
            continue

        for i in range(4):
            for j in range(4):
                if graph[i][j] == fish:
                    coor = (i, j)

        x, y = coor

        current_d = directions[fish]
        while not moveable(fish, x, y, directions, graph):
            
            rotate(fish, directions)
            if current_d == directions[fish]:
                move = False


        if move:
            dx, dy = x + movement[directions[fish]][0], y + movement[directions[fish]][1]
            graph[dx][dy], graph[x][y] = graph[x][y], graph[dx][dy]


def prey_location(fish, graph):

    for i in range(4):
        for j in range(4):
            if graph[i][j] == fish:
                return (i, j)


def backtracking(prey, food, graph, directions):

    global result

    if not prey: # 더 이상 먹을 prey가 없으면 => 상어가 집을 가야되면
        result = max(result, food)
        return

    
    for i in range(len(prey)): # prey의 개수 만큼 반복

        
        x, y = prey_location(prey[i], graph)
        food += graph[x][y]
        direction_copy = directions[:]
        map_copy = [row[:] for row in graph]
        prey_copy = shark(x, y, map_copy, direction_copy)
        backtracking(prey_copy, food, map_copy, direction_copy)
        food -= graph[x][y]
        


def shark(x, y, graph, directions): # prey의 위치가 주어지면, 그 위치로 상어가 이동해서 prey를 먹고, 그다음에 물고기가 이동을 한 다음에 상어가 먹을 수 있는 prey를 반환하는 함수

    prev_x, prev_y = prey_location(0, graph) # 상어 현재 위치

    directions[0] = directions[graph[x][y]] # 상어에게 먹힌 물고기의 방향 부여

    directions[graph[x][y]] = 0 # 먹힌 물고기 표시

    print()
    print_graph(graph)
    print()

    graph[x][y] = 0 # 상어 이동
    graph[prev_x][prev_y] = -1 # 빈 공간

    fish_move(directions, graph)

    print()
    print_graph(graph)
    print()

    prey = find_prey(x, y, directions, graph)
    if not prey:
        return False

    return prey


# initialize
result += graph[0][0]
directions[0] = directions[graph[0][0]] # 상어에게 먹은 물고기의 방향을 부여
directions[graph[0][0]] = 0 # 먹힌 물고기 표시
graph[0][0] = 0
fish_move(directions, graph)
prey = find_prey(0, 0, directions, graph)


backtracking(prey, result, graph, directions)

print(result)


