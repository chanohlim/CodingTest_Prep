'''

이진 탐색: 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로

'''

arr = [4, 6, 22, 39, 25, 345, 2, 1, 24, 56]


def quick_sort(array, start, end):

    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)



def binary_search(array, target, start, end):

    middle = (start + end) // 2

    print("middle:",middle)

    if target == array[middle]:
        return middle
    
    elif target < array[middle]:
        return binary_search(array, target, start, middle)
    
    else:
        return binary_search(array, target, middle, end)




quick_sort(arr, 0, len(arr) - 1)

print(arr)

target = int(input())

try:
    index = binary_search(arr, target, 0, len(arr) - 1)
    print(target,"의 인덱스:",index)
except RecursionError:
    print(" 리스트에 찾으시는 값이 없습니다. ")