'''

5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15

'''

N = int(input())

arr = list(map(int, input().split()))

def binary():

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        
        elif arr[mid] < mid:
            start = mid + 1
        
        else:
            end = mid - 1

    return -1

print(binary())