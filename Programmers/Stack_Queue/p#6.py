def solution(prices):
    
    stack = []
    answer = [0] * (len(prices))
    
    stack.append((prices[0], 0))
    
    for time in range(1, len(prices)):
        now = prices[time]
        prev = stack[-1][0]
        
        if now >= prev:
            stack.append((now, time))
        
        else:
            while prev > now:
                t = stack.pop()[1]                    
                answer[t] = time - t
                
                if not stack:
                    break
                    
                prev = stack[-1][0]
            
            stack.append((now, time))
            
        
    for p, t in stack:
        answer[t] = len(prices) - (t + 1)
        
        
    return answer