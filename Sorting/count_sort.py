'''

계수 정렬(Count Sort): 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘

데이터의 값이 무한한 범위를 가질 수 있는 실수형 데이터이면 사용하기 어려움.
일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있음.

'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

max_val = array[0]

for i in array: # 최댓값 구하기
    if i > max_val:
        max_val = i

cnt_list = [0 for i in range(max_val + 1)]

for i in array:
    cnt_list[i] += 1

for i in range(len(cnt_list)):
    for j in range(cnt_list[i]):
        print(i, end = " ")
