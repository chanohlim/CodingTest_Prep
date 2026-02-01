'''

퀵 정렬: 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬

1/2 + 1/4 + ... + 1/n => log2n의 시간복잡도


left랑 right가 엇갈리는 지점이 퀵정렬의 핵심

while array[left] <= array[pivot] and left < end: => 피벗보다 큰 값을 찾는 과정
    left +=1

=> start+1 ~ left-1 은 피벗보다 작은 값으로 확정(계속 스왑을 했으니)

while array[right] >= array[pivot] and right > start + 1:
    right -= 1

=> right+1 ~ end 는 피벗보다 큰 값으로 확정(계속 스왑)

만약 left랑 right가 엇갈리면=> left > right

start+1 < right-1 < left-1 은 피벗보다 작은 값, right값 역시 pivot보다 작다.
따라서 start+1 ~ right은 피벗보다 작은 값으로 확정
right+1 ~ end는 피벗보다 큰 값으로 확정
따라서 right의 위치에 pivot값이 들어가야한다!

'''


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):

    # list 크기가 1이면
    if start >= end:
        return

    pivot = start # 피벗의 초깃값은 배열의 첫 원소
    left = start + 1 # 왼쪽은 피벗값 + 1
    right = end # 오른쪽은 배열의 끝값

    while left <= right: # 엇갈리는 즉시 반복문 탈출

        print(array)

        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 이중 while 문을 사용해서 먼저 피벗보다 작은 데이터를 찾아놓고, 그 다음에 큰 데이터를 찾아놓는 방식

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        else: # 엇갈리지 않았다면 피벗보다 작은 데이터와 큰 데이터의 위치를 서로 교체
            array[left], array[right] = array[right], array[left]

        # 엇갈리면 array[right]은 pivot 값을 가르키는 상태. 따라서 피봇 값 기준 왼쪽 리스트와 오른쪽 리스트로 분해하려면 right 값 기준으로 -1 +1

    
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)