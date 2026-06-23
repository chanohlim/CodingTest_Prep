'''

10
5
10
15
20
25
30
35
40
45
50

100

'''
import heapq

N = int(input())

cards = []
for i in range(N):
    cards.append(int(input()))

total = 0
heapq.heapify(cards)

while N >= 2:
    print(cards)

    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    total += (a + b)
    heapq.heappush(cards, a + b)

    N -= 1

print(total)
