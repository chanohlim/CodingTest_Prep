'''

7
15 11 4 8 5 2 4

2

'''

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * (n)

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))