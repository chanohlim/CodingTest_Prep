x = int(input())

d = [0] * 30001

for i in range(2, x+1):

    d[i] = d[i - 1] + 1 # 먼저 1을 빼기

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1) # 1을 뺏을 때 연산의 횟수와 i를 2로 나눴을때 연산의 횟수를 비교해서 최솟값을 다시 저장
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

    print('i:',i,'최소 연산 횟수:',d[i])

print(d[x])
