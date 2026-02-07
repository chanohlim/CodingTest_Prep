'''

전보

단방향 그래프, 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나간다.
도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며, 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

입력 조건
N M C => 도시의 개수(30,000), 통로의 개수(200,000), 메시지를 보내고자 하는 도시 C
X Y Z => 도시 X에서 도시 Y로의 통로를 통해 메시지가 전달되는 시간이 Z

3 2 1
1 2 4
1 3 2


출력 조건
도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간 출력

2 4

'''

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
N, M, C = map(int, input().split())

graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


def dijkstra(start):

    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:

        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0]))

dijkstra(C)

cnt = 0
max_dist = 0
for dist in distance:

    if dist != INF and dist != 0:
        cnt += 1
        if dist > max_dist:
            max_dist = dist


print(cnt, max_dist)