'''

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

'''

n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        