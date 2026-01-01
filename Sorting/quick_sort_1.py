array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [i for i in tail if i <= pivot] # 분할된 왼쪽 부분
    right_side = [i for i in tail if i > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 파이썬의 특성을 활용한 퀵 정렬
# 포인터를 활용한 정렬이 아닌, 함수형 정렬 (인덱스를 이동시키면서 하는 정렬 X)
# 공간 복잡도 매우 커짐 => 비효율적
