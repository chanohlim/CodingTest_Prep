'''

10 500
93 181 245 214 315 36 185 138 216 295

497

'''
from sys import stdin
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = 0

def backtracking(start, l, sum):

    global result

    if sum > M:
        return
    
    if l == 3:
        result = max(result, sum)

    for i in range(start, N):
        sum += arr[i]
        backtracking(i+1, l+1, sum)
        sum -= arr[i]

def comb():
    
    a = []

    for c in combinations(arr, 3):
        if sum(c) > M:
            continue
        a.append(sum(c))

    return max(a)

print(comb())
