'''

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

'''

from sys import stdin
input = stdin.readline

from collections import deque
from utils.print_graph import print_graph


N = int(input())
K = int(input())

mx = [-1, 0, 1, 0]
my = [0, -1, 0, 1]

class Snake:

    def __init__(self):
        self.body = deque()
        self.body.append((0, 0))
        self.d = 3 # 초기 방향값: 3(오른쪽)

    

apples = []

for i in range(K):
    x, y = map(int, input().split())
    apples.append((x, y))

directions = deque()
L = int(input())

for i in range(L):
    a, b = input().split()
    directions.append((int(a), b))


graph = [ [0] * N for i in range(N)]

snake = Snake()

for apple in apples:
    x, y = apple
    graph[x-1][y-1] = 2

alive = True
time = 1

x, y = snake.body[-1]
graph[x][y] = 1

while True:


    print_graph(graph)

    if directions and time == directions[0][0]:
        d = directions.popleft()[1]

        if d == 'L':
            snake.d = (snake.d + 1) % 4
        elif d == 'D':
            snake.d = (snake.d - 1) % 4



    dx, dy = x + mx[snake.d], y + my[snake.d]

    if dx < 0 or dx >= N or dy < 0 or dy >= N:
        break

    if graph[dx][dy] == 1:
        break


    if graph[dx][dy] == 0:
        snake.body.append((dx, dy))
        a, b = snake.body.popleft()

        graph[dx][dy] = 1
        graph[a][b] = 0

    if graph[dx][dy] == 2:
        snake.body.append((dx, dy))
        graph[dx][dy] = 1

    x, y = snake.body[-1]
    time += 1



print(time+1)






    