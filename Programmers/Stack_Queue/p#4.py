from collections import deque

def solution(priorities, location):
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    priorities.sort(reverse = True)
    p = deque(priorities)
    
    cnt = 0
    
    while q:
        now, loc = q.popleft()
        if now == p[0]:
            p.popleft()
            cnt += 1
            if loc == location:
                return cnt
            else:
                continue
                
        q.append((now, loc))
            
            
        