from time import sleep

answer = int(1e9)

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

movement1 = [ # horizontal
    [(-1, 0), (-1, 0)], # 0
    [(1, 0), (1, 0)],   # 1
    [(0, -1), (0, -1)], # 2
    [(0, 1), (0, 1)],   # 3
    [(0, 0), (1, -1)],  # 4
    [(-1, 1), (0, 0)],  # 5
    [(1, 1), (0, 0)],   # 6
    [(0, 0), (-1, -1)]  # 7
]

movement2 = [ # vertical
    [(-1, 0), (-1, 0)], # 0
    [(1, 0), (1, 0)],   # 1
    [(0, -1), (0, -1)], # 2
    [(0, 1), (0, 1)],   # 3
    [(0, 0), (-1, -1)],  # 4
    [(1, 1), (0, 0)],  # 5
    [(0, 0), (-1, 1)],   # 6
    [(1, -1), (0, 0)]  # 7
]

current = [[0, 0], [0, 1]]

def print_graph(arr):
    print()
    
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()
        
    print()
    
def moveable(i, N):
    global current

    print(current, i, end = ' ')
    
    if current[0][0] == current[1][0]: # horizontal
        state = 0
        print('horizontal!', end = ' ')
    else:
        state = 1
        print('vertical!', end = ' ')
    
    if state == 0: # horizontal
        current.sort(key = lambda x: x[1])
        left, right = current
        
        left[0] += movement1[i][0][0]
        left[1] += movement1[i][0][1]
        right[0] += movement1[i][1][0]
        right[1] += movement1[i][1][1]
        
        current = [left, right]
        
        
    elif state == 1: # vertical
        current.sort()
        top, bottom = current
        
        top[0] += movement2[i][0][0]
        top[1] += movement2[i][0][1]
        bottom[0] += movement2[i][1][0]
        bottom[1] += movement2[i][1][1]
        
        current = [top, bottom]

    print(current, end = ' ')
        
    
    if (current[0][0] < 0 or current[0][0] >= N - 1
        or current[0][1] < 0 or current[0][1] >= N - 1
        or current[1][0] < 0 or current[1][0] >= N - 1
        or current[1][1] < 0 or current[1][1] >= N - 1): # out of range
        
        print(False)
        return False
    
    if ( (board[current[0][0]][current[0][1]] == 1)
        or (board[current[1][0]][current[1][1]] == 1)): # wall
        
        print(False)
        return False
    
    print(True, current)
    return True
        
    
def backtracking(time, N, board):
    
    global answer, current
    
    if time > 8:
        return
    
    left, right = current
    
    if ( (left[0] == N - 1 and left[1] == N - 1)
        or (right[0] == N - 1 and right[1] == N - 1)):
        
        answer = min(answer, time)
        return
    
    
    for i in range(8):
        
        prev = current
        print(prev)
        
        if not moveable(i, N): # not moveable
            current = prev # rollback
            continue
            
        board[current[0][0]][current[0][1]] = 2
        board[current[1][0]][current[1][1]] = 2
        
        #print_graph(board)
        
        backtracking(time + 1, N, board)
        
        
        board[current[0][0]][current[0][1]] = 0
        board[current[1][0]][current[1][1]] = 0
        current = prev # rollback for another recursion
    

def solution(board):
    global answer
    
    N = len(board)
    
    backtracking(0, N, board)
    
    
    return answer

solution(board)