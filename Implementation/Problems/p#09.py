def solution(s):
    
    l = len(s)
    
    answer = l
    
    for cut in range(1, l//2 + 1):
        
        string = ''
        cnt = 1
        prev = s[:cut]
        i = 0
        
        
        for i in range(cut, l, cut):
            
            now = s[i:i+cut]
            
            if prev == now:
                cnt += 1
            else:
                string += (str(cnt) if cnt > 1 else '') + prev
                prev = now
                cnt = 1
                
                
        string += (str(cnt) if cnt > 1 else '') + prev    
        answer = min(answer, len(string))
        
    
    return answer