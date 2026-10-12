from collections import deque

def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[0])
    q = deque(routes)
    
    while q:
        
        enter, exit = q.popleft()
        
        while q and q[0][0] <= exit:
            if q[0][1] < exit:
                enter, exit = q.popleft()
            else:
                q.popleft()
            
        answer += 1
    
    
    return answer