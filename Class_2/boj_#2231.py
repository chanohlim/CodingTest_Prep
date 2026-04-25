'''


216

198

'''


n = int(input())
a = len(str(n))


for i in range(1, n+1):
    arr = str(i)

    result = i

    for digit in arr:
        result += int(digit)
    
    if result == n:
        print(i)
        break

    if i == n:
        print(0)
