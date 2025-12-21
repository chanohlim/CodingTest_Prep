'''
Implementation.ex의 Docstring

입력 예시:
4 4
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1



출력 예시:
3


'''

n,m = map(int, input().split())
a, b, d = map(int, input().split())

map_data = list()

for i in range(n):
    map_data.append(list(map(int, input().split())))

directions = [(-1,0), (0,1), (1,0), (0,-1)] # 북, 동, 남, 서 => 캐릭터가 바라보는 방향
cnt = 1

# a, b = 현재 좌표
# da, db = 바라보는 방향의 좌표

while True:

    if d == 0: # 시선 방향 변화 (반시계방향)
        d = 3
    else:
        d -= 1


    da = a + directions[d][0]
    db = b + directions[d][1]

    if da >= n or da < 0 or db >= m or db < 0:
        continue

    if map_data[da][db] == 0:
        map_data[a][b] = 1
        a, b = da, db
        cnt += 1




