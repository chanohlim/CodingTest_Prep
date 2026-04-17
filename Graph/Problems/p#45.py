'''

최종 순위 다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	17930	7931	5620	42.281%
문제
올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다. 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.

올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다. (작년에는 순위를 발표했다) 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.

창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 올해 순위를 만드는 프로그램을 작성하시오. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우도 모두 찾아내야 한다.

입력
첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.
출력
각 테스트 케이스에 대해서 다음을 출력한다.

n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

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

복습할 땐 인접 행렬로 풀어보자!
이렇게 간선 수가 많고, 간선의 추가, 삭제, 또는 스위칭이 있으면 인접 행렬이 훨씬 자연스러운 선택

'''
from collections import deque
from sys import stdin
input = stdin.readline

def topology(graph, indegree, n):

    flag = False


    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:

        if len(q) > 1:
            flag = True

        now = q.popleft()

        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)

    if len(result) != n:
        return False

    if flag:
        return '?'
    
    return result


T = int(input())

for t in range(T):
    N = int(input())

    graph = [[] for i in range(N + 1)]
    indegree = [0] * (N + 1)

    team = list(map(int, input().split()))
    rank = [0] * (N + 1)

    for i in range(N):
        rank[team[i]] = i + 1

    for i in range(N):
        for j in range(i+1, N):
            graph[team[i]].append(team[j])
            indegree[team[j]] += 1


    change = int(input())
    for c in range(change):
        a, b = map(int, input().split())
        
        if rank[a] < rank[b]: # a의 rank가 b보다 높으면
            
            graph[a].remove(b) # a => b로 가는 경로 제거
            graph[b].append(a)
            
            indegree[b] -= 1
            indegree[a] += 1

        else:

            graph[b].remove(a)
            graph[a].append(b)

            indegree[a] -= 1
            indegree[b] += 1

    
    result = topology(graph, indegree, N)

    if result is False:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end = ' ')
        print()

