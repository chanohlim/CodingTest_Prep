'''

위상 정렬: 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'

1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    i. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 제거한다.
    ii. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.


입력:
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4


출력:
1 2 5 3 6 4 7
'''

from collections import deque

V, E = map(int, input().split())

graph = [[] for i in range(V + 1)]
indegree = [0] * (V + 1)

for i in range(E):
    
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1




def topology():

    result = list()
    queue = deque()
    
    for i in range(1, V + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        
        now = queue.popleft()
        result.append(now)
        
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)

    return result


result = topology()

if len(result) != V:
    print("사이클 존재.")
else:
    for i in result:
        print(i, end = ' ')

print(graph)