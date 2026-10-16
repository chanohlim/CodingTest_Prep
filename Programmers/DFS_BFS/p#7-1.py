from collections import deque

def solution(game_board, table):

    
    answer = 0
    
    n = len(game_board)
    
    # process table
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
                pieces.append(bfs((i, j), table, n))
                
            if game_board[i][j] == 0:
                empty.append(bfs((i, j), game_board, n))
                
    pieces.sort(key=lambda x:sum([sum(r[:]) for r in x]))
    empty.sort(key=lambda x:sum([sum(r[:]) for r in x]))
                
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
                
                if isEqual(e, piece):
                    answer += sum([sum(row[:]) for row in pieces[i]])
                    possible = True
                    break
                else:
                    piece = shift_to_top_left(rotate(piece))
                    
            if possible:
                used[i] = True
                break
            
                    
    return answer

def shift_to_top_left(graph):
    n = len(graph)
    min_x, min_y = n, n
    
    # 1이 존재하는 가장 작은 x, y 좌표 찾기
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                
    # (0, 0) 위치로 당긴 새로운 격자 생성
    new_graph = [[0] * n for _ in range(n)]
    for i in range(min_x, n):
        for j in range(min_y, n):
            if graph[i][j] == 1:
                new_graph[i - min_x][j - min_y] = 1
                
    return new_graph


def isEqual(graph1, graph2):
    
    n = len(graph1)
    
    for i in range(n):
        for j in range(n):
            if graph1[i][j] != graph2[i][j]:
                return False
            
    return True

def bfs(start, graph, n):
    
    piece = [[0] * n for i in range(n)]
    
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    
    min_x, max_x, min_y, max_y = 50, -1, 50, -1
    x, y = start
    
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    piece[x][y] = 1
    
    while q:
        x, y = q.popleft()
        min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
        
        for k in range(4):
            dx, dy = x + mx[k], y + my[k]
            
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue
                
            if graph[dx][dy] == 1:
                continue
                
            q.append((dx, dy))
            graph[dx][dy] = 1
            piece[dx][dy] = 1
        
    
    size = max(max_x - min_x, max_y - min_y) + 1
    
    new_piece = [[0] * size for i in range(size)]
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            new_piece[i - min_x][j - min_y] = piece[i][j]
    
    return new_piece

def rotate(graph):
    
    n = len(graph)
    
    new_graph = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_graph[j][n-i-1] = graph[i][j]
            
    return new_graph
    