import time
# 맵 생성
n,m = map(int, input().split())
i,j,v = map(int, input().split())
cnt = 0
movecnt = 0

directions = [(-1,0),(0,1),(1,0),(0,-1)]

gamemap = list()
map_flag = [[0 for i in range(m)]for j in range(n)]

for k in range(n):
    gamemap.append( tuple( input().split()) )

map_flag[i][j] = 1

def rotate_left(v):
    print("왼쪽으로 회전!")
    # 왼쪽으로 회전
    if v > 0:
        v -= 1 # directions => 왼쪽으로 회전
    else:
        v = 3 # v = 0일 때 왼쪽으로 회전

    print(f'방향:{v}')
    return v



print(map_flag)

while (1):
    print(f'현위치: ({i},{j})')

    v1 = rotate_left(v)
    print("왼쪽 슬쩍 보기")
    ni = i + directions[v1][0]
    nj = j + directions[v1][1]

    print(f'본 위치: ({ni},{nj})')

    if ni < 0 or ni >= m or nj < 0 or nj >= n: # 맵 범위 밖으로 간다면
        print('맵 범위 밖@')
        v = rotate_left(v) # 왼쪽으로 회전
        if cnt < 2:
            cnt += 1 # 회전 카운터 증가
        else:
            if gamemap[ni - directions[v][0]][nj - directions[v][1]] == '0':
                print('육지로 복귀!')
                i -= directions[v][0]
                j -= directions[v][1]
                movecnt += 1
                cnt = 0 # 카운터 리셋
            else:
                break
        print()
        continue

    elif gamemap[ni][nj] == '1': # 왼쪽으로 회전해서 전진한 곳이 바다일 때
        print('바다다!')
        v = rotate_left(v)
        if cnt < 2:
            cnt += 1 # 회전 카운터 증가
        else:
            if gamemap[ni - directions[v][0]][nj - directions[v][1]] == '0':
                print('육지로 복귀!')
                i -= directions[v][0]
                j -= directions[v][1]
                movecnt += 1
                cnt = 0 # 카운터 리셋
            else:
                break
        print()
        continue


    if gamemap[ni][nj] == '0' and map_flag[ni][nj] != 1:
        v = rotate_left(v)
        print('move')
        movecnt += 1
        cnt = 0
        i,j = ni,nj
        map_flag[i][j] = 1
    else:
        print('갔던 육지야!')
        v = rotate_left(v)
        print(map_flag)

    time.sleep(0.5)
    print()



print(movecnt)

