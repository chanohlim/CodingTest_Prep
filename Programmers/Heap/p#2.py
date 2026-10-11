from collections import deque
import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    
    disk_pq = []
    
    for i in range(len(jobs)):
        jobs[i].append(i)
        
    jobs.sort()
    jobs = deque(jobs)
    
    start, duration, i = jobs.popleft()
    heapq.heappush(disk_pq, (duration, start, i))
    
    return_time = [0] * n
    time = 0
    
    while jobs or disk_pq:
        
        if not disk_pq:
            start, duration, i = jobs.popleft()
        else:
            duration, start, i = heapq.heappop(disk_pq)
            
        if start <= time:
            time += duration
        else:
            time = start + duration
            
        return_time[i] = time - start
            
        if jobs:    
            while jobs[0][0] <= time:
                start, duration, i = jobs.popleft()
                heapq.heappush(disk_pq, (duration, start, i))
                if not jobs:
                    break
    
    
    
    
    return sum(return_time) // n