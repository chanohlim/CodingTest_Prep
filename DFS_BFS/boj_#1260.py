
'''
#1260

DFS와 BFS
 
시간 제한	메모리 제한	    제출	    정답	    맞힌 사람	    정답 비율
2 초	    128 MB	  351679	 143251	      84444	       39.249%

문제)
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력:
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력:
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

입력 예시:
4 5 1
1 2
1 3
1 4
2 4
3 4

출력 예시:
1 2 4 3
1 2 3 4
'''

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range (N+1)]
visited = [False] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):

    if not visited[v]:
        
        visited[v] = True
        print(v, end = ' ')
        graph[v].sort()

        for i in graph[v]:
            dfs(graph,i,visited)


def bfs(graph, v, visited):

    queue = deque([v])

    visited[v] = True

    while queue:

        v = queue.popleft()
        print(v, end = ' ')
        graph[v].sort()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



dfs(graph, V, visited)
print()

visited = [False] * (N+1)

bfs(graph, V, visited)
print()