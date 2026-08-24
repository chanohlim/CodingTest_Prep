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


def topology(N, graph, indegree):

    q = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        now = q.popleft()
        result.append(now)

        for node in graph[now]:

            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)

        if len(q) > 1: # indegree가 0이 되는게 여러개면 순서가 불분명하므로 '?' 반환 => now를 pop했으니, 원소의 개수가 2 이상이면 순서가 불분명하다.
            return '?'
        

    if len(result) != N: # 사이클 발생했으므로, 데이터에 일관성이 없다
        return 'IMPOSSIBLE'

    answer = ''
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
        if a in graph[b]: # 원래 b가 a보다 등수가 높았으면
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1


    result = topology(n, graph, indegree)
    print(result)

    