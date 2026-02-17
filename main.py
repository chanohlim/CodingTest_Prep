n = 5
build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):

    answer = []

    graph = [[0 for i in range(n+1)] for i in range(n+1)]


    for inst in build_frame:

        x, y, a, b = inst

        if b == 1:
            build(graph, x, y, a)

        if b == 0:
            remove(graph, x, y, a)

    for j in range(n+1):

        if graph[n][j] == 1:
            dfs(n, graph, n, j, answer)

    
    answer.sort(key = lambda x: (x[0], x[1], x[2]))

    return answer

def build(graph, x, y, a):

    if a == 0:
        build_col(graph, x, y)

    if a == 1:
        build_roof(graph, x, y)


def build_col(graph, x, y):

    n = len(graph)

    if y == 0: # 바닥에서 기둥 세우기
        graph[n - y - 1][x] = 1
        graph[n - y - 2][x] = 1
    elif graph[n - y - 1][x] != 0: # 기둥 또는 보에 기둥 세우기
        graph[n - y - 1][x] += 1
        graph[n - y - 2][x] = 1
    else:
        return

def build_roof(graph, x, y):

    n = len(graph)

    if graph[n - y - 1][x] != 0: # 기둥 또는 보 위에 설치하는거라면

        if y != 0 and graph[n - y][x] != 0: # 기둥 위에 바로 설치하는거라면
            graph[n - y - 1][x] += 1
            graph[n - y - 1][x + 1] += 1

        elif graph[n - y - 1][x + 1] != 0: # 보 위에 설치하는거라면
            graph[n - y - 1][x] += 1
            graph[n - y - 1][x + 1] += 1
        
        else:
            return
    elif x != n-1 and graph[n - y - 1][x + 1] != 0: # 기둥이 오른쪽에 있다면

        if graph[n - y][x + 1] != 0:
            graph[n - y - 1][x] += 1
            graph[n - y - 1][x + 1] += 1
        else: # 기둥이 아니라 보라면
            return

def remove(graph, x, y, a):

    if a == 0:
        remove_col(graph, x, y)

    if a == 1:
        remove_roof(graph, x, y)

def remove_col(graph, x, y):

    n = len(graph) # n - y - 1, x 가 현재 i,j

    if graph[n - y - 1][x] == 1: # 받치고 있는게 없음
        graph[n - y - 1][x] -= 1
        graph[n - y - 2][x] -= 1
    else:
        if graph[n - y - 2][x] == 3: # 양쪽으로 이어져있는 보를 받치고 있으면
            graph[n - y - 1][x] -= 1
            graph[n - y - 2][x] -= 1

    return
    
    


def remove_roof(graph, x, y):

    n = len(graph)

    if graph[n - y - 1][x + 1] == 2 and graph[n - y - 2][x + 1] != 0: # 기둥이 보에 의존해서 세워졌을 때
        return
    
    if graph[n - y - 1][x] == 2 and x > 0 and graph[n - y - 1][x - 1] != 2 and graph[n - y - 2][x] != 0:
        return
    
    if graph[n - y][x] == 0: # 보 아래 기둥이 없을 때
        if graph[n - y][x + 1] == 0 or (x >= 2 and graph[n - y][x - 2]): # 보가 사라지면 양 옆 보가 기둥으로부터 지지를 받지 못해지면
            return

    graph[n - y - 1][x] -= 1
    graph[n - y - 1][x + 1] -= 1


move_i = [-1, 0]
move_j = [0, 1] # 오른쪽으로 가면 보, 위로 가면 기둥

def dfs(n, graph, i, j, answer):

    x, y = j, n - i
    a = 0


    for k in range(2):

        next_i = i + move_i[k]
        next_j = j + move_j[k]

        if next_i >= 0 and next_j <= n:
            if graph[next_i][next_j] != 0:

               
                graph[i][j] -= 1
                graph[next_i][next_j] -= 1

                if k == 0: # 기둥
                    a = 0
                else: # 보
                    a = 1

                answer.append([x, y, a])
                dfs(n, graph, next_i, next_j, answer)
                break

print(solution(n, build_frame1))