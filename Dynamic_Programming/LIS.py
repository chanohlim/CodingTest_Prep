'''

가장 긴 증가하는 부분 수열: Longest Increasing Subsequence


'''

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n # 모든 dp배열 원소를 1로 초기화

# dp[i]의 뜻: a[i]로 끝나는 증가 배열 중 가장 긴 부분 수열(LIS)

def LIS(n):

    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
    return max(dp)


def bisect_lis(n):
    
    lis = []
    
    for x in a:
        pos = bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x

    print(lis)
    return len(lis)

ans1 = LIS(n)
ans2 = bisect_lis(n)

print(ans1, ans2)