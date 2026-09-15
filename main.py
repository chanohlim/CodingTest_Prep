from collections import deque

def solution(board):
    
    n = len(board)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append( (0, {(0,0), (0,1)}) )
    visited = []
    
    while q:
        
        distance, now = q.popleft()
        left, right = now

        x1, y1 = left
        x2, y2 = right
        
        if (x1 == n-1 and y1 == n-1) or (x2 == n-1 and y2 == n-1):
            return distance
        
        visited.append((left, right))
        
        for k in range(4):
            dx1, dx2, dy1, dy2 = x1 + dx[k], x2 + dx[k], y1 + dy[k], y2 + dy[k]
            
            if (dx1 < 0 or dx1 >= n) or (dx2 < 0 or dx2 >= n) or (dy1 < 0 or dy1 >= n) or (dy2 < 0 or dy2 >= n):
                    continue
                    
            if ( (dx1, dy1), (dx2, dy2) ) in visited:
                continue
                
            if board[dx1][dy1] == 1 or board[dx2][dy2] == 1:
                continue
                
            q.append( (distance + 1, (dx1, dy1), (dx2, dy2)) )
        
        if x1 == x2: # horizontal
            
            for k in [-1, 1]:
                if x1 + k < 0 or x1 + k >= n: continue

                if (board[x1 + k][y1] == 0) and ( sorted(( (x1 + k, y1), (x1, y1) )) not in visited):
                    q.append( (distance + 1, (x1 + k, y1), (x1, y1)) )
                    
                if (board[x2 + k][y2] == 0) and ( sorted(( (x2 + k, y2), (x2, y2) )) not in visited):
                    q.append( (distance + 1, (x2 + k, y2), (x2, y2)) )
                    
        if y1 == y2: # vertical

            for k in [-1, 1]:
                if y1 + k < 0 or y1 + k >= n: continue

                if (board[x1][y1 + k] == 0) and ( sorted(( (x1, y1 + k), (x1, y1))) not in visited):
                    q.append( (distance + 1, (x1, y1 + k), (x1, y1)) )
                    
                if (board[x2][y2 + k] == 0) and ( sorted(( (x2, y2 + k), (x2, y2) )) not in visited):
                    q.append( (distance + 1, (x2, y2 + k), (x2, y2)) )

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))