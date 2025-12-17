n = int(input())
plans = list(input().split())

coor_x = 1
coor_y = 1


dx = [0,0,-1,1]
dy = [-1,1,0,0]
moves = ['L', 'R', 'U', 'D']

for plan in plans:
    
    for i in range(moves):

        if plan == moves[i]:
            coor_x += dx[i]
            coor_y += dy[i]
        


print(coor_a, coor_b)