def is_one(n):
    while n > 0:

        if n % 5 == 2:
            return False
        
        n = n // 5
    
    return True

def solution1(n, l, r):
    answer = 0

    for i in range(l-1, r):
        if is_one(i):
            answer += 1

    
    return answer

def solution2(n, l, r):

    if n == 0:
        return 1
    
    answer = 0

    block = 5 ** (n-1)

    for i in range(5):
        start = i * block + 1
        end = (i+1) * block

        if (l > end) or (r < start): # 만약 현재 블록 범위에 [l, r] 구간이 들어가지 않는다면
            continue

        if i == 2: # 3번째 블록이라면(0이니까 스킵)
            continue

        new_l = max(l, start) - start + 1 # 블록 내에서의 인덱스로 다시 설정
        new_r = min(r, end) - start + 1 # 블록 내에서의 인덱스로 재설정

        answer += solution2(n-1, new_l, new_r)

    return answer

print(solution2(2, 4, 18))