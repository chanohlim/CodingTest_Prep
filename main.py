'''

5
3 2 1 1 9

8

'''
from sys import stdin
input = stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1

for coin in data:

    if coin > target:
        break

    target += coin

print(target)