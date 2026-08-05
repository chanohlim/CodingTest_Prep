'''

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

45

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

55

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

20

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

90

'''

N = int(input())
arr = []

dp = [0] * (N + 1)

for i in range(N):
    t, p = map(int, input().split())
    arr.append((t, p)) # arr[i]: i+1일의 상담 일정표


for i in range(N-1, -1, -1):
    t, p = arr[i]

    if i + t > N:
        dp[i] = dp[i + 1] # 만약 상담을 하지 못하는 경우면, 상담을 안하는 경우로 값 변경(어차피 최댓값이므로)
    
    else:
        dp[i] = max(dp[i + 1], p + dp[i + t]) # 선택 안하는 경우와 선택하는 경우

print(dp)