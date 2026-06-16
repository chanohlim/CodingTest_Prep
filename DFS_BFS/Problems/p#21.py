'''

2 20 50
50 30
20 40

1

2 40 50
50 30
20 40

0

2 20 50
50 30
30 40

1

3 5 10
10 15 20
20 30 25
40 22 10

2

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

3

'''
from collections import deque
from time import sleep

N, L, R = map(int, input().split())

A = []
movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    A.append(list(map(int, input().split())))

def print_graph(arr):
    
    print()
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()
    print()


def bfs(start, N, country, L, R):

    global moved

    i, j = start
    cnt = 1

    q = deque()
    q.append((i, j))
    B[i][j] = country

    population = A[i][j]
    
    while q:
        
        i, j = q.popleft()
        B[i][j] = country # 방문 처리 (연합 처리)

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            if (L <= abs(A[i][j] - A[di][dj]) <= R) and (B[di][dj] == 0): # 연합 조건
                population += A[di][dj]
                B[di][dj] = country
                q.append((di, dj))
                cnt += 1
    
    if cnt > 1:
        moved = True

    return (population//cnt)


answer = 0

while True:

    moved = False

    B = [[0] * N for i in range(N)]

    country = 1
    p = []

    for i in range(N):
        for j in range(N):
            if B[i][j] == 0:
                population = bfs((i,j), N, country, L, R)
                p.append(population)
                country += 1


    for i in range(N):
        for j in range(N):
            A[i][j] = p[B[i][j] - 1]


    #if country == N*N + 1:
    if not moved:
        break

    answer += 1

                
print(answer)