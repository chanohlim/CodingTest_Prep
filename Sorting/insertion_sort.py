'''

삽입 정렬: 특정한 데이터를 적합한 위치에 삽입

=> 현재 기준 왼쪽은 오름차순으로 정렬되어있다고 가정, 따라서 자기보다 왼쪽에 있는 데이터가 작으면 멈춘다.

정렬이 어느 정도 되어있으면 다른 알고리즘에 비해 굉장히 빨라진다.

'''

arr = [7, 5, 4, 8, 9, 0, 2, 1, 6, 3]

for idx in range(1, len(arr)):
    print("idx =",idx)
    while (arr[idx] <= arr[idx-1]) and (idx > 0):
        arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
        idx -= 1
        print(arr)


print(arr)