n, k = map(int, input().split())
result = 0

while (n > k):

    target = (n // k) * k # n이 k의 배수가 되는 수로 만들기 => target: n의 초깃값에서 k의 배수가 되는 가장 가까운 수
    print(target)
    result += (n - target) # result = result + (n - target)
    n = target

    result += 1
    n //= k

result += (n - 1)
print(result)