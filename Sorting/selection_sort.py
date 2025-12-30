'''

정렬: 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

선택 정렬: 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정 반복
'''

arr = list(map(int, input().split()))



for i in range(len(arr)):
    max_idx = i
    max_val = arr[max_idx] 

    for j in range(i,len(arr)):
        print(i,j)
        if arr[j] >= max_val:
            max_val = arr[j]
            max_idx = j
        
    print("max: ",max_val, max_idx)
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
    print(arr)



print(arr)