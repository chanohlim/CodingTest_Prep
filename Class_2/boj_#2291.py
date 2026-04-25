def fnc(n):
    return (3*(n*n) - 3*n + 1)

N = int(input())

if N == 1:
    print(1)
    
else:
    i = 1
    while True:
        if fnc(i-1) < N <= fnc(i):
            print(i)
            break
        i += 1