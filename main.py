'''

5
2 3 1 2 2

2

'''
from sys import stdin
input = stdin.readline

N = int(input())

explorers = list(map(int, input().split()))

explorers.sort()

cnt = 0


for i in explorers:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(cnt)

