'''

미로 탈출

N x M 크기의 직사각형 미로에 갇혀있다.
초기 위치: (1,1)
미로의 출구: (N,M)
한 번에 한 칸씩 이동할 수 있다. 
괴물이 있는 부분은 0, 괴물이 없는 부분은 1

=> 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. (시작 칸과 마지막 칸을 모두 포함해서 계산)

입력 조건: 첫째 줄에 두 정수 N,M(4 <= N,M <= 200), N:세로 M:가로, 시작 칸과 마지막 칸은 항상 1

출력 조건: 첫째 줄에 최소 이동 칸의 개수를 출력한다.

입력 예시:
5 6
101010
111111
000001
111111
111111

출력 예시:
10

'''

from collections import deque

N, M = map(int, input().split())

graph = list()

for i in range(N):
    graph.append(list(map(int, input())))

di_list = [-1, 1, 0, 0]
dj_list = [0, 0, -1, 1]


def bfs(i, j):

    q = deque()
    q.append((i, j))

    while q:

        i, j = q.popleft()
            
        for k in range(4):

            di = i + di_list[k]
            dj = j + dj_list[k]

            if (0 <= di < N) and (0 <= dj < M):

                if graph[di][dj] == 1: # 미방문한 노드라면
                    graph[di][dj] += graph[i][j]
                    q.append((di, dj))
                
bfs(0,0)


print(graph[N-1][M-1])