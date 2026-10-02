def solution(numbers):
    
    answer = 0
    perm = set()
    
    for i in range(1, len(numbers) + 1):
        backtracking('', perm, numbers, i)
        
    for n in perm:
        
        if n < 2:
            continue
            
        isPrime = True
        for i in range(2, n//2 + 1):
            if n % i == 0:
                isPrime = False
                break
                
        if isPrime:
            answer += 1
    
    return answer

def backtracking(path, perm, numbers, end):
    
    if len(path) == end:
        perm.add(int(path))
        
    for i in range(len(numbers)):
        path += numbers[i]
        temp_numbers = numbers[:i] + numbers[i+1:]
        backtracking(path, perm, temp_numbers, end)
        path = path[:-1]
        