n,k = map(int, input().split(' '))
cnt = 0

while (n):
    if( n % k == 0 ):
        n = n // k
        cnt += 1
    else: # 바로 n % k == 0이 만족되도록 연산
        a = n % k
        n -= a
        cnt += a

print(cnt-1)