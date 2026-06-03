'''

입력 예시1:
4 4 2 1
1 2
1 3
2 3
2 4

출력 예시1:
4

입력 예시2:
4 3 2 1
1 2
1 3
1 4

출력 예시:
-1

입력 예시:
4 4 1 1
1 2
1 3
2 3
2 4

출력 예시:
2
3
'''

from sys import stdin
input = stdin.readline

from collections import deque

INF = int(1e9)

N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
distance = [INF] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b로 갈 수 있음

def bfs(start, K):
    
    q = deque()
    q.append(start)

    distance[start] = 0

    possible_city = []


    while q:
        now = q.popleft()

        for node in graph[now]:

            if distance[node] == INF:
                distance[node] = distance[now] + 1

                if distance[node] == K:
                    possible_city.append(node)

                q.append(node)


    if possible_city:
        return possible_city
    else:
        return -1

possible_city = bfs(X, K)

if possible_city == -1:
    print(-1)
else:
    possible_city.sort()
    for city in possible_city:
        print(city)