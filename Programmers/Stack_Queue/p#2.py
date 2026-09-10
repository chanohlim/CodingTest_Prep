from collections import deque

def solution(progresses, speeds):
    
    answer = []
    
    time = deque()
    l = len(progresses)
    
    for i in range(l):
        
        data = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            data += 1
            
        time.append(data)
    
    cnt = 1
    
    passed = time.popleft()
    
    while time:
        
        if time[0] <= passed:
            cnt += 1
            time.popleft()
        else:
            answer.append(cnt)
            passed = time.popleft()
            cnt = 1
            
    answer.append(cnt)
    
    return answer