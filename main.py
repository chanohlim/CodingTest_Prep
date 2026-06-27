'''

입력 예시:
4 6
19 15 10 17

출력 예시:
15

'''

N, M = map(int, input().split())

arr = list(map(int, input().split()))


def binary(start, end, M):

    while start <= end:

        mid = (start + end) // 2 # 절단기에 설정할 수 있는 높이
        
        total = 0

        for cake in arr:
            if cake > mid:
                total += cake - mid

        if total >= M: # 조건 만족 => 절단기 높이 높여서 최적화
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    
    return answer
            

print(binary(0, max(arr), M))
