from collections import deque

def solution(game_board, table):
    
    answer = 0
    
    n = len(game_board)
    
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                table[i][j] = 0
            else:
                table[i][j] = 1
    
    pieces = []
    empty = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                pieces.append(bfs((i,j), table, n))
                
            if game_board[i][j] == 0:
                empty.append(bfs((i,j), game_board, n))
    
    pieces.sort(key=lambda x:len(x))
    empty.sort(key=lambda x:len(x))
    
    used = [False] * len(pieces)
    
    for e in empty:
        
        possible = False
        for i in range(len(pieces)):
            
            if used[i]:
                continue
                
            piece = pieces[i]
            
            if len(piece) != len(e):
                continue
            
            for k in range(4):
                if piece == e:
                    answer += len(piece)
                    possible = True
                    used[i] = True
                    break
                else:
                    piece = rotate(piece)
            
            if possible:
                break
                
    return answer
                
def rotate(piece):
    
    new_piece = [[y, -x] for x, y in piece]
    
    return shift(new_piece)
    
                
def bfs(start, graph, n):
    
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    
    q = deque()
    x, y = start
    piece = []
    
    q.append(start)
    graph[x][y] = 1
    piece.append([x, y])
    
    while q:
        
        x, y = q.popleft()
        
        for k in range(4):
            dx, dy = x + mx[k], y + my[k]
            
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue
                
            if graph[dx][dy] == 1:
                continue
                
            q.append((dx, dy))
            graph[dx][dy] = 1
            piece.append([dx, dy])
    
    piece = shift(piece)
    piece.sort()
    
    return piece
        
def shift(piece):
    
    min_x = 50
    min_y = 50
    
    for i in range(len(piece)):
        x, y = piece[i]
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        
    new_piece = [[x - min_x, y - min_y] for x, y in piece]
    new_piece.sort()
        
    return new_piece