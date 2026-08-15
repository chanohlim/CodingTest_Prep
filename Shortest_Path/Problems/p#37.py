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
from print_graph import print_graph

input = stdin.readline

INF = int(1e9)


n = int(input())
m = int(input())

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있습니다. => 함정
    
print_graph(graph)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print_graph(graph, 1, 1)