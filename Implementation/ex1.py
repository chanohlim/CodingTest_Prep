# 입력 받기

n = int(input())
travel = list(input().split())

# 구현

coor_x = 1
coor_y = 1

for dir in travel:

    if dir == 'L':
        if coor_x - 1 > 0:
            coor_x -= 1
    if dir == 'R':
        if coor_x + 1 < n:
            coor_x += 1
    if dir == 'U':
        if coor_y - 1 > 0:
            coor_y -= 1
    if dir == 'D':
        if coor_y + 1 < n:
            coor_y += 1

print(coor_y,coor_x)