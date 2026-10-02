def solution(arr):
    answer = []
    
    current = arr[0]
    
    for i in arr:
        if i != current:
            answer.append(current)
            current = i
            
    answer.append(i)
    
    return answer