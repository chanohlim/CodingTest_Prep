import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        heapq.heappush(scoville, a + (b*2))
        answer += 1
        
        if len(scoville) < 2:
            if scoville[0] > K:
                break
                
            return -1
    
    return answer