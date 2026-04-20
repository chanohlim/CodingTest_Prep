'''

5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

14

4 2 6
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
4 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3

26

5 4 1
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

-1

5 4 10
0 0 0 0 3
0 0 0 0 0
1 2 0 0 0
0 0 0 0 4
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

-1

'''


def find_dir(shark):

    i, j = current_loc[shark]

    possible = []

    for k in range(1, 5): # 현재 상어 위치 기준 상 하 좌 우 탐색
        di, dj = i + movement[k][0], j + movement[k][1]
        
        if di < 0 or di >= N or dj < 0 or dj >= N:
            continue

        shark_no, time = trace[di][dj]

        if shark_no == 0: # 아무 냄새가 없는 칸이면
            possible.append((di, dj, k)) # 좌표와 방향
        elif 


def move(shark):

    # 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동, 자신의 냄새를 그 칸에 뿌림
    di, dj = find_dir(shark)

    # 1. 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡고 2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 선정
    # 가능한 칸이 여러개면 우선순위에 따름 => 보고 있는 방향에 따라 우선순위가 다르고 상어마다 다름
    # 방금 이동한 방향이 보고 있는 방향이 됨
    # 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 사망



N, M, K = map(int, input().split())

map = [] # 실제로 상어가 움직이는 map
trace = [[(0,0)] * N for i in range(N)] # 상어의 냄새와 지속 시간 기록
shark_dir = [0] # 상어가 보는 방향 관리
movement = [(0,0), (-1, 0), (1, 0), (0, -1), (0, 1)] # 1: 위 2: 아래 3: 왼쪽 4: 오른쪽
current_loc = [0] * (N + 1)
time = 0

for i in range(N):
    map.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if map[i][j] != 0:
            current_loc[map[i][j]] = (i, j)
            


temp = list(map(int, input().split()))

for i in range(M):
    shark_dir.append(temp[i]) # shark i의 방향: shark_dir[i]


# priority[0 ~ 3] : shark 1 ...
# shark1: 0 1 2 3   shark2: 4 5 6 7     shark3: 8 9 10 11       shark4: 12 13 14 15
# (dir-1) + (4 * (N-1)) => shark3이고 dir=3 => 2 + 8
priority = []

for i in range(4*M):
    priority.append(list(map(int, input().split())))




