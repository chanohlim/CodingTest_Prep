'''

정렬: 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

선택 정렬: 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정 반복
'''

arr = list(map(int, input().split()))


def selection_desc(arr):
    for i in range(len(arr)):
        max_idx = i

        for j in range(i+1,len(arr)):
            print(i,j)
            if arr[j] >= arr[max_idx]:
                max_idx = j
            
        print("max: ",arr[max_idx], max_idx)

        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
        print(arr)

    return arr


def selection_inc(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1,len(arr)):
            print(i,j)
            if arr[j] <= arr[min_idx]:
                min_idx = j
            
        print("max: ",arr[min_idx], min_idx)

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(arr)

    return arr



print("내림차순 선택 정렬:", selection_desc(arr))
print("오름차순 선택 정렬:", selection_inc(arr))
