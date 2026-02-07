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
import copy
from collections import deque
import sys

INF = int(1e9)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
table = [[INF] * (N + 1) for i in range(N + 1)]


for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    table[a][b] = 1
    table[b][a] = 1

for i in range(1, N+1):
    table[i][i] = 0

X, K = map(int, input().split())


def dijkstra(start, end):

    distance = [INF] * (N + 1)

    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for node in graph[now]:
            cost = dist + 1

            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(pq, (cost, node))

    return distance[end]

def floyd(start, end):

    table_ = copy.deepcopy(table)

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                table_[i][j] = min(table_[i][j], table_[i][k] + table_[k][j])

    return table_[start][end]

def bfs(start):

    distance = [INF] * (N + 1)
    visited = [False] * (N + 1)
    
    q = deque()
    visited[start] = True
    distance[start] = 0

    q.append(start)
    
    while q:
        
        now = q.popleft()
        print(f'now:{now}')
        print(distance)

        for node in graph[now]:

            if not visited[node]:
                visited[node] = True
                q.append(node)
                distance[node] = distance[now] + 1

    return(distance)


print(dijkstra(1, K) + dijkstra(K, X))
print(floyd(1, K) + floyd(K, X))
print(bfs(1))