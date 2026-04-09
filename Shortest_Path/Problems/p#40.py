'''

6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

'''

from collections import deque

INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, N):

    q = deque()
    q.append(start)
    distance[start] = 0

    while q:
        now = q.popleft()
        for node in graph[now]:

            if distance[node] != INF: # 이미 방문한 노드이므로 방문X
                continue

            distance[node] = distance[now] + 1
            q.append(node)

    max_val = 0
    max_node = N
    cnt = 0

    for i in range(N, 0, -1):

        if distance[i] > max_val:
            max_val = distance[i]
            max_node = i
            cnt = 1

        elif distance[i] == max_val:
            max_node = i
            cnt += 1

    return max_node, max_val, cnt

a, b, c = bfs(1, N)

print(a, b, c)


        

        


