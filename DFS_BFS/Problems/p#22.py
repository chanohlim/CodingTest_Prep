from collections import deque

def get_next_pos(pos, board):
    
    next_pos = []
    pos = list(pos) # set is not subscriptable -> need to change to list
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    for k in range(4):
        dx1, dx2, dy1, dy2 = x1 + dx[k], x2 + dx[k], y1 + dy[k], y2 + dy[k]
        
        if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
            next_pos.append({(dx1, dy1), (dx2, dy2)})
            
    if x1 == x2:
        
        for k in [-1, 1]:
            if board[x1 + k][y1] == 0 and board[x2 + k][y2] == 0:
                next_pos.append({(x1, y1), (x1 + k, y1)})
                next_pos.append({(x2, y2), (x2 + k, y2)})
                
    if y1 == y2:
        
        for k in [-1, 1]:
            if board[x1][y1 + k] == 0 and board[x2][y2 + k] == 0:
                next_pos.append({(x1, y1), (x1, y1 + k)})
                next_pos.append({(x2, y2), (x2, y2 + k)})
                
    return next_pos
        

def solution(board):
    
    n = len(board)
    # padding => less compares
    new_board = [[1] * (n+2) for i in range(n+2)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                new_board[i+1][j+1] = 0
                
    q = deque()
    pos = frozenset({(1,1), (1,2)})
    distance = 0
    q.append((distance, pos))
    
    visited = set()
    visited.add(pos)
    
    while q:
        
        distance, pos = q.popleft()
        
        if (n,n) in pos:
            return distance
        
        for next_pos in get_next_pos(pos, new_board):
            
            if next_pos in visited:
                continue
                
            q.append((distance + 1, next_pos))
            visited.add(frozenset(next_pos))
            
                