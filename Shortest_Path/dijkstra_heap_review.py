'''

입력:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2


출력:
0
2
3
1
2
4

'''

import heapq

INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):

    pq = []
    distance[start] = 0
    heapq.heappush(pq,(0, start))

    while pq:

        dist, now = heapq.heappop(pq) # now 노드까지의 거리 dist

        if dist > distance[now]: # 과거의 기록이면, 더 갱신될 노드가 없으므로 패스
            continue

        for node in graph[now]:
            
            cost = dist + node[1] # node[0]까지의 거리

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq,(cost, node[0]))


dijkstra(start)
print(distance)
