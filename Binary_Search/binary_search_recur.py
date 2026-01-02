'''

이진 탐색: 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하면서 범위를 좁혀나가서 타깃을 찾는 탐색

재귀함수 형태로 작성된 코드

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

    print("start:",start,"end:",end)

    if start > end: # 이진 탐색은 항상 start 와 end 사이에 타깃이 존재하는 불변의 법칙을 지킨다.
        return None # 만약 start > end가 된다면 start 와 end 사이의 범위가 애초에 존재하지 않으니 이는 곧 '타깃이 배열에 없다'로 귀결

    middle = (start + end) // 2

    print("middle:",middle,"value:",array[middle])

    if target == array[middle]: # 타깃이 미들 값과 동일하면 미들 값 리턴
        return middle
    
    elif target < array[middle]:
        return binary_search(array, target, start, middle - 1) # 미들 값보다 타깃이 작으면, 시작부터 미들값 전 값까지만 확인
    
    else:
        return binary_search(array, target, middle + 1, end) # 미들 값보다 타깃이 크면, 미들 값 직후부터 끝 인덱스까지 확인




quick_sort(arr, 0, len(arr) - 1)

print(arr)

target = int(input())

index = binary_search(arr, target, 0, len(arr) - 1)

if index:
    print(index)
else:
    print("리스트 안에 찾으시는 값이 존재하지 않습니다.")