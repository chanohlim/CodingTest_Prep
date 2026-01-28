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

'''

from collections import deque

N = int(input())

indegree = [0] * (N + 1)
time = [0] * (N + 1)
graph = [[] for i in range(N + 1)] # graph[i][0]: i번 강의의 수강 시간

for i in range(1, N+1):
    
    input_list = list(map(int, input().split()))
    input_list.pop()

    for j in input_list:
        graph[i].append(j) # 1번 강의: 시간, 선수강의1, 선수강의2, ...
        indegree[i] += 1
    
    indegree[i] -= 1


def topology_sort():

    q = deque()
    result = list()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    

    while q:

        now = q.popleft()
        print(now)
        result.append(now)

        print(graph[now])
        print(q)

        for i in range(1, len(graph[now])):
            node = graph[now][i]
            indegree[node] -= 1
            
            if indegree[node] == 0:
                q.append(node)

    return result

print(topology_sort())


    
    




