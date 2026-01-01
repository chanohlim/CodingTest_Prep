
n = int(input())
data = list()

for i in range(n):
    data.append(int(input()))

def quick_sort(array, start, end):

    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while right >= left:
        while left <= end and array[left] >= array[pivot]:
            left += 1

        while right > start and array[right] <= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(data, 0, len(data) - 1) # 인덱스이므로 리스트의 길이에서 1을 뺌
print(data)