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
        
        now, index = heapq.heappop(pq)
        
        k -= (now-previous) * length
        length -= 1
        
        previous = now

    pq.sort(key = lambda x: x[1])
    return pq[k % length][1]
        