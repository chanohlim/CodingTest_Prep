'''

3 3
1 0 2
0 0 0
3 0 0
2 3 2

3

3 3
1 0 2
0 0 0
3 0 0
0 2 2

0

'''


from sys import stdin
input = stdin.readline

import heapq
from collections import deque

N, K = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

S, X, Y = map(int, input().split()) # S초 뒤에 arr[X][Y]에 있는 바이러스의 종류는?

pq = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            pq.append((arr[i][j], (i, j)))

def print_graph(arr):
    print()

    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()

def infect_pq(pq, K, S):

    heapq.heapify(pq)
    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:


        n, now = heapq.heappop(pq)

        if ( (n-1) // K ) == S: # 종료조건
            break

        i, j = now

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            if arr[di][dj] != 0:
                continue


            arr[di][dj] = (n-1) % K + 1
            heapq.heappush(pq, ((n+K),(di, dj)) )

q = sorted(pq)

def infect_queue(q, K, S):

    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque(q)

    while queue:


        n, second, now = queue.popleft()
        print(second)

        if second == S: # 종료조건
            break

        i, j = now

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            if arr[di][dj] != 0:
                continue

            arr[di][dj] = n
            print_graph(arr)
            queue.append((n, second+1, (di, dj)))


infect_pq(pq, K, S)
#infect_queue(q, K, S)

print(arr[X-1][Y-1])