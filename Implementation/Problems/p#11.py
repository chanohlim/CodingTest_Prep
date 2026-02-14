'''

뱀 다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	93401	41172	27836	42.554%
문제
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다.
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며.
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

예제 입력 1 
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
예제 출력 1 
9
예제 입력 2 
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
예제 출력 2 
21
예제 입력 3 
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
예제 출력 3 
13


행 = i
열 = j

matrix[i][j]

'''
import os
import time as t
from collections import deque

coor = []


def print_arr(arr):

    print()
    
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()

    print()

def move(board, d, head, time, length):
    
    i, j = head
    

    current_dir = direction_list[d]
    next_i = i + current_dir[0]
    next_j = j + current_dir[1]

    if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N: # 죽음 조건 1: 벽에 부딪히기
        return False
    
    if board[next_i][next_j] == 1: # 자기 자신일때
        return False

    if board[next_i][next_j] == 2: # 사과가 있는 좌표에 도달했으면
        length += 1
        print("apple found!")
        board[next_i][next_j] = 0
    else:
        prev_i, prev_j = coor[time - length]
        board[prev_i][prev_j] -= 1

    board[next_i][next_j] += 1
        
    return (next_i, next_j, length)

N = int(input())

board = [[0 for i in range(N)] for i in range(N)]
apple = []

K = int(input())

for i in range(K):
    
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

L = int(input())

directions = deque()
for i in range(L):
    X, C = input().split() # L: 왼쪽, D: 오른쪽
    directions.append((int(X), C))

time = 0
alive = True
d = 1
length = 1
current = (0,0)
direction_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

board[0][0] = 1

x, c = directions.popleft()
coor.append((0,0))
print_arr(board)
t.sleep(1)
os.system('clear')

while alive:
        
        time += 1

        current = move(board, d, coor[time - 1], time, length)

        if current == False:
            print("dead!")
            print(time)
            break

        coor.append((current[0], current[1]))
        length = current[2]
        
        print('time:', time)
        print_arr(board)        

        if time == x:
            if c == 'L':
                if d == 0:
                    d = 3
                else:
                    d -= 1
            else:
                if d == 3:
                    d = 0
                else:
                    d += 1
            if not directions:
                t.sleep(1)
                os.system('clear')
                continue
            x, c = directions.popleft()

        t.sleep(1)
        os.system('clear')
=