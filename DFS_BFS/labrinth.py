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

N,M = map(int, input().split())

graph = list()

for i in range(N):
    graph.append(list(map(int, input())))

i_mov = [0,0,1,-1]
j_mov = [1,-1,0,0]

def bfs(graph,i,j):

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()
        print(i,j)

        for a in range(4): # 상 하 좌 우 원소들 확인하기 => 한 좌표당 4번 연산
            di = i + i_mov[a]
            dj = j + j_mov[a]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 0:
                continue
            # 좌표를 처음 방문하는 경우에만 최단 거리 기록
            if graph[di][dj] == 1:
                graph[di][dj] = graph[i][j] + 1
                queue.append((di,dj))
        

bfs(graph,0,0)

for a in graph:
    for b in a:
        print (b, end = ' ')
    print()

print("최소 이동 수:",graph[N-1][M-1])
