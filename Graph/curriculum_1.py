'''

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

'''

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N + 1)]
indegree = [0] * (N + 1)
cost = [0] * (N + 1)

for i in range(1, N+1):
    input_list = list(map(int, input().split()))

    cost[i] = input_list[0]

    for j in input_list[1:-1]:
        graph[j].append(i) # i번 강의를 수강하기 위해 수강해야되는 강의 j => graph[j]의 노드로 i가 들어가야됨: 그래프는 항상 미래를 가르킨다!
        indegree[i] += 1



def topology_sort():

    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    # import copy, copy.deepcopy(cost) 대신
    # result는 i번 강의를 수강하기 위해 걸리는 시간
    # 초깃값은 자기 자신만 수강할 때 걸리는 시간(cost 리스트)
    result = list()
    for i in cost:
        result.append(i)

    while q:

        now = q.popleft()

        for node in graph[now]: # now가 가르키는 노드
            indegree[node] -= 1
            result[node] = max(result[node], result[now] + cost[node]) # cost는 초기 값으로 고정, result 값만 계속 갱신 => dp느낌
            # result 리스트는 하나의 강의를 수강하기 위해 선수강해야되는 강의의 수강시간을 계속 최댓값으로 갱신하는 리스트

            if indegree[node] == 0:
                q.append(node)

    return result
    
        
result = topology_sort()

for i in result[1:]:
    print(i)