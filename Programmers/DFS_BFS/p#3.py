from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    new_maps = [[0] * (m + 2) for i in range(n + 2)]
    
    for i in range(n):
        for j in range(m):
            new_maps[i+1][j+1] = maps[i][j]
            
    visited = [[False] * (m+2) for i in range(n+2)]
    
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    
    q = deque()
    q.append((1, (1,1)))
    visited[1][1] = True
    
    while q:
        
        distance, now = q.popleft()
        x, y = now
        
        if x == n and y == m:
            return distance
        
        for k in range(4):
            dx, dy = x + mx[k], y + my[k]
            if visited[dx][dy] or new_maps[dx][dy] == 0:
                continue
                
            q.append((distance + 1, (dx, dy)))
            visited[dx][dy] = True
    
    return -1