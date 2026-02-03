'''

효율적인 화폐 구성

입력 조건:
첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10000)
이후 N개의 줄에는 각 화폐의 가치가 주어진다.

출력 조건:
첫째 줄에 M원을 만들 수 있는 최소한의 화폐 개수를 출력한다.
불가능하다면 -1을 출력한다.

입력 예시:
2 15
2
3

3 4
3
5
7

출력 예시:
5

-1


경로 복원

'''

N, M = map(int, input().split())

INF = int(1e9)

dp = [INF] * (M+1)
dp[0] = 0

coins = [int(input()) for i in range(N)]

for coin in coins:

    for i in range(coin, M + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[M] != INF:
    print(dp[M])
else:
    print(-1)