'''

N	stages	                    result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	                [4,1,2,3]


'''

def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N + 1):
        
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            
            fail = count / length
            length -= count
            
        answer.append((i, fail))
        
    answer.sort(key=lambda x: -x[1])
    
        
    return [i[0] for i in answer]

'''N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]'''

N = 4
stages = [4, 4, 4, 4, 4]
# 1 2 2 2 3 3 4 6

print(solution(N, stages))

def solution2(N, stages):
    answer = []
    
    failure = [[i+1, 0] for i in range(N)]
    stages.sort()
    n = len(stages)
    
    cnt = 0
    current = 1
    i = 0
    
    while (i < len(stages)):
        
        if stages[i] == current:
            cnt += 1
            i += 1
            
        elif stages[i] > current:
            failure[current-1][1] = cnt / n
            n -= cnt
            cnt = 0
            current += 1
    
    if current != (N + 1):
        failure[current-1][1] = cnt / n
        
    
    failure.sort(key=lambda x: (-x[1], x[0]))
    
    for a,b in failure:
        answer.append(a)
    
    
    return answer