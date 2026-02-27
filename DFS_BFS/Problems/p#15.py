
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

from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(N + 1)]
distance = [-1] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):

    q = deque()
    q.append(start)
    distance[start] = 0

    while q:
        now = q.popleft()     

        for node in graph[now]:
            if distance[node] == -1: # 방문 여부 확인
                q.append(node)
                distance[node] = distance[now] + 1
                

bfs(X)
cnt = 0

for i in range (1, N + 1):
    if distance[i] == K:
        print(i)
        cnt += 1

if not cnt:
    print(-1)