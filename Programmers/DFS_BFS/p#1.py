def solution(numbers, target):
    global answer
    answer = 0
    
    backtracking(0, numbers, target, 0)
    
    return answer


def backtracking(i, numbers, target, total):
    global answer
    
    if i == len(numbers):
        if total == target:
            answer += 1
            
        return
        
    backtracking(i + 1, numbers, target, total + numbers[i])
    backtracking(i + 1, numbers, target, total - numbers[i])