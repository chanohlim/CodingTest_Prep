'''

3
10
20
40

100

'''
import heapq

N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))


if N == 1:
    print(0)

else:

    heapq.heapify(arr)
    result = 0

    while arr:

        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        result += (a + b)

        if not arr:
            break

        heapq.heappush(arr, a + b)
    
    print(result)