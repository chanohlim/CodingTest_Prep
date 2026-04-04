'''

7
15 11 4 8 5 2 4

2

'''

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

def LIS(n):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] > a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)

def bisect_LIS(n):
    lis = []

    a.reverse()

    for x in a:
        pos = bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x

    return n - len(lis)

print(bisect_LIS(n))