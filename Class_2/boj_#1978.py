'''

4
1 3 5 7

3

'''

arr = [True] * 1001

arr[0] = False
arr[1] = False

for n in range(2, len(arr)):
    if arr[n] == True:
        j = 2
        while n * j <= 1000:
            arr[n*j] = False
            j += 1

N = int(input())

numbers = list(map(int, input().split()))

result = 0

for n in numbers:
    if arr[n]:
        result += 1

print(result)