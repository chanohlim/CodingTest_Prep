'''

N	stages	                    result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	                [4,1,2,3]


'''

def solution(N, stages):
    
    answer = []
    
    stages.sort()
    count = [0] * (N + 2)

    for i in stages:
        count[i] += 1
    
    length = len(stages)
    for i in range(1, N + 1):
        length -= count[i]

        if length == 0:
            break
        
        count[i] /= length + count[i]
    
    count_index = []
    for i in range(1, N + 1):
        count_index.append((i, count[i]))
    
    count_index.sort(key = lambda x: -x[1])

    for a, b in count_index:
        answer.append(a)

    return answer

'''N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]'''

N = 4
stages = [4, 4, 4, 4, 4]
# 1 2 2 2 3 3 4 6

print(solution(N, stages))