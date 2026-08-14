str_a = input()
str_b = input()

n = len(str_a)
m = len(str_b)

# a -> b

dp = [[0] * (m + 1) for i in range(n + 1)] # 공백 포함

for i in range(1, m+1):
    dp[0][i] = i

for i in range(1, n+1):
    dp[i][0] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        if str_a[i-1] == str_b[j-1]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = min(
                dp[i-1][j], # 삭제
                dp[i][j-1], # 삽입
                dp[i-1][j-1] # 교체
            ) + 1

print(dp[n][m])

print(dp)