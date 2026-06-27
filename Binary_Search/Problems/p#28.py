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

def binary(start, end):

    if start > end:
        return -1
    
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    elif arr[mid] < mid: # 좌측은 무조건 idx보다 arr[idx]가 작음
        return binary(mid + 1, end)
    elif arr[mid] > mid: # 우측은 무조건 idx보다 arr[idx]가 큼
        return binary(start, mid - 1)

print(binary(0, len(arr) - 1))