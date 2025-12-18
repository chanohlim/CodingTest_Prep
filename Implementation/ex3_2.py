'''
입력: a1

출력: 2

8x8 체스판
나이트가 이동할 수 있는 경우의 수

오오위
오오아래

왼왼위
왼왼아래

위위오
위위왼

아래아래오
아래아래왼

총 8가지 경우의 수가 최상

  1(a)  2  3  4  5  6  7  8
1
2
3
4
5
6
7
8
'''

loc = input()

row = int(loc[1])
col = ord(loc[0]) - ord('a') + 1

move_row = [1,-1,1,-1,-2,-2,2,2]
move_col = [2,2,-2,-2,1,-1,1,-1]

cnt = 0

for i in range(8):

    nrow = row + move_row[i]
    ncol = col + move_col[i]

    if nrow < 1 or nrow > 8 or ncol < 1 or ncol > 8:
        continue

    print(nrow, ncol)
    cnt += 1

print(cnt)