'''

5 3
1
2
8
4
9

3

'''

N, C = map(int, input().split())

arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

def parametric(target):


    start = 1
    end = arr[-1] - arr[0]

    while start <= end:

        c = 1
        prev = arr[0]

        gap = (start + end) // 2

        print(start, end, gap)

        for i in range(1, N):
            if (arr[i] - prev) >= gap:
                c += 1
                prev = arr[i]

        if c < target: # gap이 너무 큼
            end = gap - 1
        elif c >= target: # gap이 작거나 적절함
            start = gap + 1
            result = gap

    return result

print(parametric(C))