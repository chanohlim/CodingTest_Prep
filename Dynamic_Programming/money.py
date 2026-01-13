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

INF = 10001 # 특정 금액을 만들 수 있는 화폐 구성이 불가능함을 뜻함

dp = [INF] * (M + 1) # 일단 구성하려는 금액보다 적은 모든 금액에 대해서 불가능함으로 초기화
dp[0] = 0 # 0원을 만들 수 있는 경우는 화폐를 하나도 사용하지 않았을 때 가능하므로 0으로 설정

choice = [0] * (M + 1) # 금액 i를 만들 때 마지막으로 선택한 화폐 단위
coin_result = [0] * (max(coins) + 1) # 금액 i를 만들 때 사용한 화폐 단위를 인덱스로 받아서 한번 사용했을 때마다 1씩 더하기

# dp 배열의 값: 인덱스 - 특정 금액(0 ~ M원)     배열 원소 - 특정 금액을 만들 수 있는 최소한의 화폐 개수

for coin in coins:
    for i in range(coin, M + 1):
        
        if (dp[i - coin]) != INF:
            print(f'dp[{i}]: {i}원일 때 화폐 최소 개수 정하기: min(dp[{i} - {coin}] + 1: {dp[i - coin] + 1}, dp[{i}]: {dp[i]})', end = ' ')
            
            if (dp[i - coin] + 1) < dp[i]:
                choice[i] = coin
                dp[i] = dp[i - coin] + 1
                print(f'최솟값: {dp[i]}')

if dp[M] == INF:
    print(-1)
else:

    min = dp[M]
    while min > 0:
        
        for coin in coins:
            min

    print(dp[M])
