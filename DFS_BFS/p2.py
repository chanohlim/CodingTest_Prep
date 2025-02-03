from collections import deque

N,M = map(int,input().split())

graph = list()

for k in range(N):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i,j):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((i,j))
    # 큐가 빌 때까지 반복
    while queue:
        i,j = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 좌표가 그래프 경계를 벗어날 경우 무시
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            # 좌표가 괴물이 위치한 곳(벽)일 경우 무시
            if graph[ni][nj] == 0:
                continue
            # 좌표를 처음 방문하는 경우에만 최단 거리 기록
            if graph[ni][nj] == 1:
                graph[ni][nj] = graph[i][j] + 1
                queue.append((ni,nj))
    # 가장 오른쪽 아래의 최단 거리 반환
    return graph[N-1][M-1]

print(bfs(0,0))
print(graph[0][0])