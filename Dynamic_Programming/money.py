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



'''

N, M = map(int, input().split())
coins = [int(input()) for i in range(N)]

INF = 10001

dp = [INF] * (M + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, M + 1):
        print(f'dp[{i}]: {i}원일 때 화폐 최소 개수 정하기: min(dp[{i} - {coin}] + 1: {dp[i - coin] + 1}, dp[{i}]: {dp[i]})', end = ' ')
        dp[i] = min(dp[i - coin] + 1, dp[i])
        print(f'최솟값: {dp[i]}')

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])
