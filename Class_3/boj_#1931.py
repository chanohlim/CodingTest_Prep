'''

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

4

6
2 2
3 3
7 10
0 2
4 4
2 10

5

'''
from sys import stdin
input = stdin.readline

N = int(input())

meeting = []

for i in range(N):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))

prev_end = meeting[0][1]
result = 1

for i in range(1, N):
    start, end = meeting[i]

    if start >= prev_end:
        result += 1
        prev_end = end

print(result)
