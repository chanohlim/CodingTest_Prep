'''

5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

'''


N, M = map(int, input().split())
K = list(map(int, input().split()))

result = 0

# bruteforce

for i in range(N):
    current_ball = K[i]

    for j in range(i+1, N):
        if K[j] != current_ball:
            result += 1

print(result)


# greedy - 가벼운 공부터 고르고, 남은 공들의 개수만큼 곱한다.

count = [0] * (N + 1)
for ball in K:
    count[ball] += 1


left = N
ans = 0

for i in range(1, N+1):
    
    left -= count[i]
    ans += count[i] * left

print(ans)