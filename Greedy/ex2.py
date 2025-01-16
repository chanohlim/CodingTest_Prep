# 데이터 입력
n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

# 그리디 법칙을 따른 연산
data.sort()
max1 = data[n-1]
max2 = data[n-2]
sum = 0

while ( m > 0 ):
    sum += max1 * k
    m -= k
    if( m >= 1):
        sum += max2
        m-= 1

print(sum)