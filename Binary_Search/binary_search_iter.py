'''

binary search iteration

'''

arr = [4, 6, 22, 39, 25, 345, 2, 1, 24, 56]
arr.sort()

print(arr)

def binary(array, target):

    start = 0
    end = len(array) - 1
    
    while start <= end: # 재귀로 하지 않고 while 반복문을 돌림으로써 시간복잡도를 줄임

        mid = (start + end) // 2

        print(start, end, mid, array[mid])

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else: # arr[mid] < target
            start = mid + 1


    return None

n = int(input())

print(binary(arr,n))