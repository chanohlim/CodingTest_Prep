# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
col = ord(input_data[0])-ord('a')+1

cnt = 0

# 나이트가 이동할 수 있는 8가지 경우의 수
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

for step in steps:

    nrow = row + step[1]
    ncol = col + step[0]

    if nrow > 8 or nrow < 1 or ncol > 8 or ncol < 1:
        continue

    cnt += 1

print(cnt)