import heapq

def solution(operations):
    
    visited = set()
    
    max_heap = []
    min_heap = []
    
    id = 0
    
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        
        if op == 'I':
            
            heapq.heappush(max_heap, (-n, id))
            heapq.heappush(min_heap, (n, id))
            id += 1
            
        elif op == 'D':
            
            if n == 1: # remove max
                while max_heap and (max_heap[0][1] in visited):
                    heapq.heappop(max_heap)
                    
                if not max_heap:
                    continue
                    
                now = heapq.heappop(max_heap)[1]
                visited.add(now)
                
            elif n == -1: # remove min
                while min_heap and (min_heap[0][1] in visited):
                    heapq.heappop(min_heap)
                
                if not min_heap:
                    continue
                    
                now = heapq.heappop(min_heap)[1]
                visited.add(now)
    
    max_n = 0
    while max_heap:
        
        if max_heap[0][1] in visited:
            heapq.heappop(max_heap)
            
            if not max_heap:
                max_n = 0
                break
            
        else:
            max_n = -max_heap[0][0]
            break
    
    min_n = 0
    while min_heap:
        
        if min_heap[0][1] in visited:
            heapq.heappop(min_heap)
            
            if not min_heap:
                min_n = 0
                break
            
        else:
            min_n = min_heap[0][0]
            break
            
    return [max_n, min_n]
    
    