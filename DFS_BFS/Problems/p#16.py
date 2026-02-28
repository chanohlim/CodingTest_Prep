'''

배워갈 점:
1. 조합으로 벽 세우기 후 완전탐색 => 백트래킹으로도 가능(두 번째 시도때 해보자)
2. dfs 대신 bfs로 해야지 재귀깊이 초과할 위험도 없고 더 빠르다. 어차피 그래프 완전탐색은 둘 다 똑같이 기능한다.
3. 2차원 배열 복사는 deepcopy보다, copy = [row[:] for row in graph] 로 하는게 더 빠르다.
4. bfs 하고 0을 일일히 카운트하기보다, bfs를 돌면서 확산되는 개수를 카운팅하고, 그걸 return 받아서 수식으로 계산하는게 훨씬 빠름

7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

9

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

3

7 7
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 1 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

'''

from sys import stdin
from itertools import combinations
from collections import deque
import time

input = stdin.readline

N, M = map(int, input().split())

graph = []
blank = []
viruses = []

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            blank.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

move = [(-1,0), (1,0), (0,1), (0,-1)]

def dfs(i, j, graph):

    for k in range(4):
        di, dj = i + move[k][0], j + move[k][1]

        if 0 <= di < N and 0 <= dj < M:
            
            if graph[di][dj] == 0:
                graph[di][dj] = 2
                dfs(di, dj, graph)

def bfs(graph):

    q = deque(viruses)
    infected = 0

    while q:
        i, j = q.popleft()
        for k in range(4):
            di, dj = i + move[k][0], j + move[k][1]

            if 0 <= di < N and 0 <= dj < M:

                if graph[di][dj] == 0:
                    graph[di][dj] = 2
                    infected += 1
                    q.append((di, dj))

    return infected



result = 0

for wall in combinations(blank, 3): # 리스트에 저장하지 않고 바로 이터레이션

    map_copy = [row[:] for row in graph] # deepcopy보다 가벼운 복사법

    for coor in wall:
        map_copy[coor[0]][coor[1]] = 1

    cnt = len(blank) - 3 - bfs(map_copy)

    result = max(result, cnt)

print(result)