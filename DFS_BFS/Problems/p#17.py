'''

3 3
1 0 2
0 0 0
3 0 0
2 3 2

3

3 3
1 0 2
0 0 0
3 0 0
0 2 2

0

'''

from sys import stdin
import heapq

input = stdin.readline

N, K = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    

S, X, Y = map(int, input().split())

pq = []

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            heapq.heappush(pq, (graph[i][j], (i, j)))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_graph(graph):
    for i in graph:
        for j in i:
            print(j, end = ' ')
        print()

def spread(graph, pq, endtime):

    time = 0

    if endtime == 0:
       return

    while pq:

        print()
        print('time:', time)
    
        for l in range(len(pq)):

            virus, coor = heapq.heappop(pq)
            i, j = coor

            for k in range(4):
                di, dj = i + move[k][0], j + move[k][1]

                if 0 <= di < N and 0 <= dj < N:
                    if graph[di][dj] == 0:
                        graph[di][dj] = virus - (K * time)
                        heapq.heappush(pq, (virus + K, (di, dj)))

            print()
            print_graph(graph)

        time += 1
        if time == endtime:
            break
            

    
spread(graph, pq, S)
print(graph[X-1][Y-1])