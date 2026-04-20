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
from sys import stdin
input = stdin.readline

def print_graph(arr):
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()


def time_down():
    for i in range(N):
        for j in range(N):

            shark_no, time = trace[i][j]
            
            if time > 1:
                trace[i][j] = (shark_no, time-1)
            elif time == 1:
                trace[i][j] = (0, 0) # 냄새 만료
            



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

    if not possible: # 아무 냄새가 없는 칸이 존재하지 않으면

        for k in range(1, 5): # 현재 상어 위치 기준 상 하 좌 우 탐색
            di, dj = i + movement[k][0], j + movement[k][1]
        
            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue
            
            shark_no, time = trace[di][dj]

            if shark_no == shark: # 자신의 냄새가 있는 칸이면
                possible.append((di, dj, k)) # 좌표와 방향

    current_dir = shark_dir[shark]

    for p in priority[(current_dir - 1) + (4 * (shark - 1))]: # 예) 4 2 3 1 같은 우선순위 리스트 - 우 하 좌 상 - 순
        for a in possible:
            if a[2] == p:
                return a[0], a[1], a[2] # di, dj, k
    

            



def move(shark):

    i, j = current_loc[shark] # 상어의 현재 위치


    # 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동, 자신의 냄새를 그 칸에 뿌림
    di, dj, k = find_dir(shark)

    if ocean[di][dj] != 0: # 다른 상어가 이동하려는 칸에 있으면
        if shark > ocean[di][dj]: # 현재 상어의 번호가 더 크면 현재 상어가 쫓겨남
            ocean[i][j] = 0
            current_loc[shark] = (-1, -1)
            shark_dir[shark] = 0
            return
        else:
            shark_dir[ocean[di][dj]] = 0 # 기존에 있던 상어 쫓겨남
            current_loc[ocean[di][dj]] = (-1, -1)
            ocean[di][dj] = shark
            ocean[i][j] = 0
            current_loc[shark] = (di, dj)
            shark_dir[shark] = k


    else: # 상어가 이동하려는 칸에 없으면
        ocean[di][dj] = shark
        ocean[i][j] = 0
        current_loc[shark] = (di, dj)
        shark_dir[shark] = k





N, M, K = map(int, input().split())

ocean = [] # 실제로 상어가 움직이는 map
trace = [[(0,0)] * N for i in range(N)] # 상어의 냄새와 지속 시간 기록
shark_dir = [0] # 상어가 보는 방향 관리
movement = [(0,0), (-1, 0), (1, 0), (0, -1), (0, 1)] # 1: 위 2: 아래 3: 왼쪽 4: 오른쪽
current_loc = [0] * (M + 1)
time = 0

for i in range(N):
    ocean.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if ocean[i][j] != 0:
            current_loc[ocean[i][j]] = (i, j)
            trace[i][j] = (ocean[i][j], K)
            


temp = list(map(int, input().split()))

for i in range(M):
    shark_dir.append(temp[i]) # shark i의 방향: shark_dir[i]


# priority[0 ~ 3] : shark 1 ...
# shark1: 0 1 2 3   shark2: 4 5 6 7     shark3: 8 9 10 11       shark4: 12 13 14 15
# (dir-1) + (4 * (N-1)) => shark3이고 dir=3 => 2 + 8
priority = []

for i in range(4*M):
    priority.append(list(map(int, input().split())))


print_graph(ocean)
print()
print_graph(trace)
print()


while time  <= 1000:

    time += 1
    cnt = 0

    for i in range(1, M+1):
        
        if shark_dir[i] != 0: # 상어가 쫓겨나지 않았으면
            move(i)

    time_down()

    for k in range(1, M+1): # 살아있는 상어 수 세기
        if shark_dir[k] != 0:
            i, j = current_loc[k]
            trace[i][j] = (k, K)
            cnt += 1

    print_graph(ocean)
    print()
    print_graph(trace)
    print()



    if cnt == 1:
        break


if time == 1001:

    print(-1)

else:
    print(time)

