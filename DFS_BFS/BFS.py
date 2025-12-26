'''
DFS_BFS.BFS의 Docstring

BFS: 너비 우선 탐색 => 가까운 노드부터 탐색하는 알고리즘, 선입선출 방식인 큐 자료구조 이용
실제 구현함에 있어서는 deque 라이브러리를 사용하는 것이 바람직, 수행 시간은 DFS보다 좋은 편

1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.

2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.

3) 2)번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

'''

from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):

    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)