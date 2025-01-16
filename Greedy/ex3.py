n,m = map(int, input().split(' '))
ans = 0

for i in range(n):
    ls = list(map(int, input().split(' ')))
    a = min(ls)
    ans = max(ans,a)

print(ans)
