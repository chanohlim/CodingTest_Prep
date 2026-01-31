'''
첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의
자연수가 주어지며, 각 자연수는 공백으로 구분한다.

둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는
1 이상 10,000 이하의 수로 주어진다.

입력으로 주어지는 K는 항상 M보다 작거나 같다.

입력:
5 8 3
2 4 5 4 6

출력:
46 => 6 6 6 5 6 6 6 5
'''

N, M, K = map(int, input().split())

input_list = list(map(int, input().split()))
input_list.sort()

a = input_list[-1]
b = input_list[-2]

cnt = 0
result = 0

while M:

    if cnt == 3:
        cnt = 0
        M -= 1
        print(b, end = ' ')
        result += b
        continue

    print(a, end = ' ')
    result += a
    cnt += 1
    M -= 1

print()
print(result)
