'''

rice_cake 문제를 while 반목문을 사용한 iteration 풀이

'''

N, M = map(int, input().split())
ricecake = list(map(int, input().split()))

def iter_parametric(arr, target, start, end):

    result = 0

    
    while start <= end:

        mid = (start + end) // 2
        total = 0

        for i in arr:
            if mid < i:
                total += (i - mid)


        if total >= target: # 총 합이 원하는 조건을 만족, 하지만 더 답에 가까운 mid가 있을 수 있으므로 일단 저장하고 다음 범위 탐색 
                            # => mid 값 증가시켜야 total 값 줄어듬
            start = mid + 1
            result = mid
        else:
            end = mid - 1
            
        

    return result

print(iter_parametric(ricecake, M, 0, max(ricecake)))