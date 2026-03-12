'''

150
266
427

3
1
0
2
0
0
0
2
0
0

'''

n = 1
count = [0] * 10

for i in range(3):
    n *= int(input())

for i in str(n):
    count[int(i)] += 1

for c in count:
    print(c)

