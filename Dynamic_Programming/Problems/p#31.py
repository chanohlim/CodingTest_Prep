'''

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

'''

from copy import deepcopy

def max_val (arr):

    result = arr[0][0]

    for i in arr:
        for j in i:
            if j > result:
                result = j

    return result

def input_gold(N, M):
    dp = [[0] * M for k in range(N)] 
    temp = list(map(int, input().split()))

    row = 0
    col = 0
    for j in temp:
        if col == M:
            col = 0
            row += 1

        dp[row][col] = j
        col += 1
    
    return dp

def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()

T = int(input())

movement = [(-1, 1), (0, 1), (1, 1)]

for case in range(T):

    N, M = map(int, input().split())

    dp = input_gold(N, M)
    origin = deepcopy(dp)

    for j in range(M):
        for i in range(N):
            for k in movement:
                di, dj = i + k[0], j + k[1]

                if 0 <= di < N and 0 <= dj < M:
                    dp[di][dj] = max(dp[di][dj], dp[i][j] + origin[di][dj])

    print(max_val(dp))