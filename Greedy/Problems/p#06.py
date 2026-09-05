'''

bruteforce로는 안풀리니까, 레벨 단위로 음식을 처리하는 아이디어가 핵심
그리디를 사용해 시간이 적은 음식부터 우선적으로 처리

'''

import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    
    pq = []
    l = len(food_times)
    
    prev = 0
    
    for i in range(l):
        heapq.heappush(pq, [food_times[i], i+1])
    
        
    while (pq[0][0] - prev) * l <= k:
        
        now = heapq.heappop(pq)[0]
        
        k -= l * (now - prev)
        l -= 1
        
        prev = now
            
    
    pq.sort(key=lambda x: x[1])
    answer = pq[k%l][1]
    
    return answer