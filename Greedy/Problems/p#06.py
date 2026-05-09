'''

bruteforce로는 안풀리니까, 레벨 단위로 음식을 처리하는 아이디어가 핵심
그리디를 사용해 시간이 적은 음식부터 우선적으로 처리

'''

import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    pq = []
    length = len(food_times)
    
    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i+1))
        
    previous = 0
        
    while (pq[0][0]-previous) * length <= k:
        
        now = heapq.heappop(pq)[0]
        
        k -= (now-previous) * length
        length -= 1
        
        previous = now

    pq.sort(key = lambda x: x[1])
    return pq[k % length][1]
        