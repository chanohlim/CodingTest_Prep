array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):

    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    while left <= right:

        print(array)
        
        while left <= end and array[left] <= array[pivot]: # 만약 조건문순서가 반대면 리스트 인덱스 에러 터질 수 있음
            left += 1

        while array[right] >= array[pivot] and right > start:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
        
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)