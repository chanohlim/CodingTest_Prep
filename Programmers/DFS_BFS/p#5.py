from collections import deque
from time import sleep

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    max_n = 0
    
    mx = [-1, -1, 0, 1, 1, 1, 0, -1]
    my = [0, -1, -1, -1, 0, 1, 1, 1]
    
    for rect in rectangle:
        max_n = max(max_n, max(rect))
        
    graph = [[1] * (3*max_n + 3) for i in range(3*max_n + 3) ]
    
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        
        x1 *= 3
        y1 *= 3
        x2 *= 3
        y2 *= 3
        
        
        for i in range(y1-1, y2):
            for j in range(x1-1, x2):
                graph[i][j] = 0
                
                
    new_graph = [row[:] for row in graph]
    
    for x in range(3, 3*max_n + 3):
        for y in range(3, 3*max_n + 3):
            
            if graph[x][y] == 0:

                border = False

                for k in range(8):
                    dx, dy = x + mx[k], y + my[k]
                    
                    if graph[dx][dy] == 1:
                        border = True
                        break
                
                if border:
                    continue
                    
                new_graph[x][y] = 1
    
    visited = [[False] * (3*max_n + 3) for i in range(3*max_n + 3)]
    
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    
                
    for i in new_graph:
        for j in i:
            print(j, end = ' ')
        print()
            
    q = deque()
    q.append((0, (3*characterX, 3*characterY)))
    visited[characterY][characterX] = True
    
    while q:
        
        dist, now = q.popleft()
        x, y = now

        print(dist, now)

        if 3*itemX == x and 3*itemY == y:
            return dist // 3
        
        for k in range(4):
            dx, dy = x + mx[k], y + my[k]
            if new_graph[dy][dx] == 1 or visited[dy][dx]:
                continue
                
            q.append((dist + 1, (dx, dy)))
            visited[dy][dx] = True
            
    
    
        
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
charX = 1
charY = 3
itemX = 7
itemY = 8

print(solution(rectangle, charX, charY, itemX, itemY))