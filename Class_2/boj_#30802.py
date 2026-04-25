'''

23
3 1 4 1 5 9
5 7

7
3 2

'''

N = int(input())

shirt = list(map(int, input().split()))
T, P = map(int, input().split())

a = 0

for s in shirt:
    
    if s % T != 0: quantity = (s // T) + 1
    else: quantity = (s//T)
    
    a += quantity


print(a)
print(N//P, N%P)
