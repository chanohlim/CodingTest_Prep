'''

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

'''
movement = [-1, 0, 1]

T = int(input())

for t in range(T):

    n, m = map(int, input().split())
    temp = list(map(int, input().split()))

    arr = []

    for i in range(n):
        arr.append(temp[i*m:(i+1)*m])

    dp = [[0] * m for i in range(n)]

    for i in range(n):
        dp[i][0] = arr[i][0]

    for j in range(m-1):
        for i in range(n):

            '''for k in movement:
                di, dj = i + k, j + 1

                if di < 0 or di >= n or dj < 0 or dj >= m:
                    continue

                dp[di][dj] = max(dp[di][dj], dp[i][j] + arr[di][dj])'''

            left_up = dp[i-1][j] if i>0 else 0
            left = dp[i][j]
            left_down = dp[i+1][j] if i<n-1 else 0

            dp[i][j+1] = arr[i][j+1] + max(left_up, left, left_down)

    print(max(dp[i][m-1] for i in range(n)))