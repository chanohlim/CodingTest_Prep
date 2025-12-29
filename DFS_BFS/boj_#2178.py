'''
미로 탐색
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	192 MB	255757	122041	75901	45.979%
문제
NxM크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력:
4 6
101111
101010
101011
111011

예제 출력:
15

'''

from collections import deque

N,M = map(int, input().split())

graph = list()

for i in range(N):
    graph.append(list(map(int, input())))

i_mov = [0, 0, 1, -1]
j_mov = [1, -1, 0, 0]

def bfs(graph, i,j):

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()
        
        for k in range(4):
            di = i + i_mov[k]
            dj = j + j_mov[k]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 0:
                continue

            if graph[di][dj] == 1: # 처음 방문하는 숫자 1인 노드 중
                queue.append((di,dj))
                graph[di][dj] = graph[i][j] + 1

    return graph[N-1][M-1]



print(bfs(graph,0,0))

        

