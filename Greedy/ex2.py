

# 데이터 입력
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

# 데이터 정렬
data.sort()

# 최댓값 및 두 번째 최댓값 구하기
largest = data[n-1]
large = data[n-2]

# 큰 수의 법칙 구하기

total = 0
cnt = 0

while (m > 0):

    if cnt == k:
        cnt = 0
        total += large
        m -= 1
        continue

    total += largest
    cnt += 1
    m -= 1

print(total)