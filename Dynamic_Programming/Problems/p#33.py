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

def bottom_up(N):

    schedule = [0]
    dp = [0]

    for i in range(N):
        T, P = map(int, input().split())
        schedule.append(T)
        dp.append(P)


    for i in range(1, N + 1):

        temp = []
        for j in range(1, i):
            if j + schedule[j] <= i:
                temp.append(dp[j])

        if temp:
            dp[i] += max(temp)

    result = []

    for i in range(1, N+1):
        if i + schedule[i] <= N + 1:
            result.append(dp[i])
    if result:
        print(max(result))
    else:
        print(0)
    

def top_down(N):
    t = []
    p = []
    dp = [0] * (N + 1)
    max_value = 0

    for i in range(N):
        T, P = map(int, input().split())
        t.append(T)
        p.append(P)

    for i in range(N-1, -1, -1): # N-1 ~ 0까지 거꾸로 확인
        time = t[i] + i

        if time <= N:
            dp[i] = max(p[i] + dp[time], max_value)
            max_value = dp[i]
        
        else:
            dp[i] = max_value

    print(max_value)

top_down(N)



