'''

3
10
20
40

100

'''

N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

if N < 2:
    result = 0
else:
    result = arr[0] + arr[1]

for i in range(2, N):
    result += result + arr[i]

print(result)