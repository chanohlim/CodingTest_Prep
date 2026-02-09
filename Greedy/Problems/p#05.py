'''

#05 볼링공 고르기

입력:
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

출력:
8

25


N, M = map(int, input().split())

count = [0] * (M + 1)

input_list = list(map(int, input().split()))

for i in input_list:
    count[i] += 1

result = 0

for i in count:
    if i <= 1:
        continue
    result += i*(i-1)//2

answer = (N * (N-1) // 2) - result

print(answer)

'''

