def possible(answer):
    
    for struct in answer:
        
        x, y, a = struct
        
        
        if a == 0: # pillar
            if ( 
                (y == 0)
                 or ( (x-1, y, 1) in answer)
                 or ( (x, y, 1) in answer)
                 or ( (x, y-1, 0) in answer)):
                continue
            
            
        elif a == 1: # bo
            if ( 
                ( (x, y-1, 0) in answer) 
                 or ( (x+1, y-1, 0) in answer) 
                 or ( ( (x-1, y, 1) in answer) and ( (x+1, y, 1) in answer)) ):
                
                continue
                
        return False # continue x => False
    
    return True
            
        
            
    
    
    

def solution(n, build_frame):
    answer = set()
    
    for instruction in build_frame:
        
        x, y, a, b = instruction
        

        if b == 0: # delete

            answer.remove((x, y, a))

            if not possible(answer):
                answer.add((x, y, a))
                continue


        elif b == 1: # install

            answer.add((x, y, a))

            if not possible(answer):
                answer.remove((x, y, a))
                continue

    answer = sorted(answer, key=lambda x:(x[0], x[1], x[2]))
    
    return [list(x) for x in answer]