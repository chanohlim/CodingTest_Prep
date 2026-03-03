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

N, L, R = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

temp = [([0] * N) for i in range(N)]
sum_pop = [0 for i in range(N*N + 1)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def unite(i, j, nation):

    
    q = deque()
    q.append((i, j))
    temp[i][j] = nation

    cnt = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            di, dj = i + move[k][0], j + move[k][1]

            if (di < 0) or (di >= N) or (dj < 0) or (dj >= N):
                continue

            if temp[di][dj] == 0:
                if L <= abs(graph[i][j] - graph[di][dj]) <= R: # 국경선이 열리는 조건
                    sum_pop[nation] += graph[di][dj]
                    temp[di][dj] = nation
                    cnt += 1
                    q.append((di, dj))

    return cnt


def print_graph(graph):

    print()

    for i in graph:
        for j in i:
            print(j, end = ' ')
        print()




def population():


    nation = 1

    for i in range(N):
        for j in range(N):
            if temp[i][j] == 0:
                sum_pop[nation] += graph[i][j]
                cnt = unite(i, j, nation)
                sum_pop[nation] = sum_pop[nation] // cnt
                nation += 1


    for i in range(N):
        for j in range(N):
            graph[i][j] = sum_pop[temp[i][j]]

    return nation


cnt = 0

    
while True:

    temp = [([0] * N) for i in range(N)]
    sum_pop = [0 for i in range(N*N + 1)]

    nation = population()
    if nation == (N*N + 1):
        break

    temp = [([0] * N) for i in range(N)]
    sum_pop = [0 for i in range(N*N + 1)]

    cnt += 1

print(cnt)
