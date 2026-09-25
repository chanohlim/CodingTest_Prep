from utils.print_graph import print_graph

a = input()
b = input()

# a => b

n = len(a)
m = len(b)

dp = [[0] * (m + 2) for i in range(n + 2)]


for i in range(n):
    dp[i+2][0] = a[i]
    dp[0][i+2] = b[i]


for i in range(2, n+2):
    dp[i][1] = i-1

for i in range(2, m+2):
    dp[1][i] = i-1


for i in range(2, n + 2):
    for j in range(2, m + 2):
        if a[i-2] == b[j-2]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = min(
                dp[i-1][j], # 삭제
                dp[i][j-1], # 삽입
                dp[i-1][j-1] # 교체
            ) + 1

print_graph(dp)