'''

3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3

5 3 2 4 1
2 3 1
IMPOSSIBLE

'''
from sys import stdin
input = stdin.readline

from collections import deque


def topology(N, indegree, graph):

    q = deque()
    result = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

        if len(q) > 1:
            return "?"

    if len(result) != N:
        return "IMPOSSIBLE"
    else:
        answer = ""
        for i in result:
            answer += str(i)
            answer += ' '

        return answer

T = int(input())
for t in range(T):

    n = int(input())

    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)
    rank = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]] += 1


    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())
        if a in graph[b]: # b -> a, b>a
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1

    answer = topology(n, indegree, graph)
    print(answer)


    
            