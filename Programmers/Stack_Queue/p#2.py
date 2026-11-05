from collections import deque

def solution(s):
    
    q = deque(s)
    cnt = 0
    
    while q:
        now = q.popleft()
        if now == '(':
            cnt += 1
        else:
            cnt -= 1
            
        if cnt < 0:
            return False
        
    if cnt != 0:
        return False

    return True