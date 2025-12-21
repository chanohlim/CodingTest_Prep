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
sea_cnt = 0


# a, b = 현재 좌표
# da, db = 바라보는 방향의 좌표

while True:

    if d == 0: # 시선 방향 변화 (반시계방향)
        d = 3
    else:
        d -= 1


    da = a + directions[d][0]
    db = b + directions[d][1]

    print(da, db)

    if da >= n or da < 0 or db >= m or db < 0: # 맵 밖이면 스킵
        sea_cnt += 1
        continue

    if map_data[da][db] !=  0: # 바다면 스킵
        print("바다다!")
        sea_cnt += 1
        continue

    if map_data[da][db] == 0: # 바라보는 방향이 가지 않은 육지
        
        print("육지다!")
        map_data[a][b] = 2 # 현재 있는 칸은 방문 표시
        a, b = da, db # 바라보는 칸으로 이동
        print(a, b,'로 이동 완료!')
        cnt += 1 # 이동 횟수 + 1

    
    if sea_cnt > 3:

        map_data[a][b] = 2
        da = a + directions[d-2][0]
        db = b + directions[d-2][1]
        if map_data[da][db] != 1:
            a, b = da, db
        else:
            break

print(cnt)

print(map_data)





