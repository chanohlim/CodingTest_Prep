'''

3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

'''
from sys import stdin
input = stdin.readline


N, M = map(int, input().split())

a = set()
answer = []
result = 0

for i in range(N):
    a.add(input())

for i in range(M):

    name = input()
    if name in a:
        answer.append(name)
        result += 1

answer.sort()

print(result)
for name in answer:
    print(name)