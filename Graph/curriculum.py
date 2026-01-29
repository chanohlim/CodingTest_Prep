'''

커리큘럼

동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램 작성
동시에 여러 개의 강의를 들을 수 있다고 가정한다.

입력 조건:
N
강의시간 선수강번호 ... -1

출력 조건:
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력


입력 예시:
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

=> 1 2 3 4 5

출력 예시:
10
20
14
18
17
'''

from collections import deque

N = int(input())

indegree = [0] * (N + 1)
cost = [0] * (N + 1)
graph = [[] for i in range(N + 1)]

for i in range(1, N+1):
    
    input_list = list(map(int, input().split()))
    input_list.pop()

    cost[i] = input_list[0]
    
    length = len(input_list)

    for j in range(1, length):
        graph[i].append(input_list[j])

    indegree[i] = length - 1



def topology_sort(graph, cost, indegree):

    q = deque()
    result = list()

    for i in range(1, N+1):
        print(indegree[i])
        if indegree[i] == 0:
            q.append(i)

    print('hi')
    

    while q:

        now = q.popleft()
        result.append(now)

        max_cost = 0

        for i in range(1, N+1):
            
            if now in graph[i]:
                indegree[i] -= 1
                print(i)
            
                if indegree[i] == 0:
                    q.append(i)
                    for node in graph[i]:
                        if cost[node] > max_cost:
                            max_cost = cost[node]

                    cost[i] += max_cost

            

        

    return result

print(topology_sort(graph, cost, indegree))

for i in range(1, N+1):
    print(cost[i], end = ' ')
