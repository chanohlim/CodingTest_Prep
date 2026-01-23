'''

1번에서 K(소개팅), K에서 X(판매)까지의 최단거리를 각각 출력해서 더하면 된다. 

입력 조건:
N M => 회사의 개수, 경로의 개수
연결된 두 회사의 번호들
X K

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4

출력 조건:
A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

3

-1

'''

import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

X, K = map(int, input().split())

def dijkstra(start, target):

    distance = [INF] * (N + 1)

    distance[start] = 0
    pq = []

    heapq.heappush(pq, (0, start))

    while pq:
        
        dist, now = heapq.heappop(pq)
        
        if dist > distance[now]:
            continue

        for node in graph[now]:

            cost = dist + node[1] # cost = 현재 노드까지의 최단거리 + 다음 노드까지의 거리
            
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq,(cost, node[0]))

    return distance[target]
    

a, b = dijkstra(1, K), dijkstra(K, X)

if a == INF or b == INF:
    print(-1)
else:
    print(a + b)

