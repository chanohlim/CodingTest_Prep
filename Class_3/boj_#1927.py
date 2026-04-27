'''

9
0
12345678
1
2
0
0
0
0
32

'''
from sys import stdin
input = stdin.readline

import heapq

T = int(input())

pq = []

for i in range(T):

    X = int(input())

    if X == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))

    else:
        heapq.heappush(pq, X)
