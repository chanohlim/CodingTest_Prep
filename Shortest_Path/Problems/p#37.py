'''

5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0

'''

from sys import stdin
input = stdin.readline

INF = int(1e9)

n = int(input())
e = int(input())

distance = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(1, n+1):
    distance[i][i] = 0

for i in range(e):
    a, b, cost = map(int, input().split())
    distance[a][b] = min(distance[a][b], cost)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print(0, end = ' ')
        else:
            print(distance[i][j], end = ' ')
    print()