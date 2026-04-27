'''

5
3 1 4 3 2

32

'''
from sys import stdin
input = stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

time = 0
answer = 0

for t in arr:
    time += t
    answer += time

print(answer)