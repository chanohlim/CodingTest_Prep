'''

7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3

'''

N, x = map(int, input().split())
arr = list(map(int, input().split()))

def binary_start(target):

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        elif arr[mid] == target:
            if mid > 0 and arr[mid - 1] != target:
                return mid
            else:
                end = mid - 1

    return None

def binary_end(target):

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        elif arr[mid] == target:
            if mid < N - 1 and arr[mid + 1] != target:
                return mid
            else:
                start = mid + 1

    return None

a = binary_start(x)
b  = binary_end(x)

if a and b:
    print(b - a + 1)
elif a or b:
    print(1)
else:
    print(-1)