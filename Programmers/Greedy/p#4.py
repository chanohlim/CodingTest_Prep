from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    q = deque(people)
    
    while q:
        
        l = limit
        l -= q.popleft()
        
        if q and l - q[-1] >= 0:
            q.pop()
            
        answer += 1
    
    return answer