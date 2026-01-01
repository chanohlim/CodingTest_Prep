'''

두 배열의 원소 교체

두 배열 A, B가 주어지면, K번의 바꿔치기를 통해 배열 A의 합이 최대가 되게 하여 그 합을 출력하면 된다.

입력 예시:
5 3
1 2 5 4 3
5 5 6 6 5

출력 예시:
26

'''

N, K = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

for i in range(K):
    
    arr_a.sort()
    arr_b.sort(reverse=True)

    arr_a[0], arr_b[0] = arr_b[0], arr_a[0]


sum = 0

for i in arr_a:
    sum += i

print(sum)
    