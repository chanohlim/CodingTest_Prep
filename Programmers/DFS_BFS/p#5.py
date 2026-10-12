from collections import deque
from print_graph import print_graph

def solution(rectangle, characterX, characterY, itemX, itemY):

    max_n = 30
    graph = [[8] * max_n for i in range(max_n)]

    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: 2*x, rect)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                else:
                    if graph[i][j] != 0:
                        graph[i][j] = 1

    print_graph(graph)

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]


    charX, charY, iX, iY = characterX*2, characterY*2, itemX*2, itemY*2

    q = deque()
    q.append((0, (charX,charY)))

    while q:

        dist, now = q.popleft()
        x, y = now

        if x == iX and y == iY:
            return dist // 2

        for k in range(4):
            dx, dy = x + mx[k], y + my[k]

            if graph[dx][dy] != 1:
                continue

            q.append((dist + 1, (dx, dy)))
            graph[dx][dy] = 0



        
rectangle1 = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
rectangle2 = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
rectangle3 = [[2,1,7,5],[6,4,10,10]]
rectangle4 = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
charX = 1
charY = 3
itemX = 7
itemY = 8

print(solution(rectangle4, charX, charY, itemX, itemY))