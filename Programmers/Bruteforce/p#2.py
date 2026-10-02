def solution(answers):
    answer = []
    
    i1, i2, i3 = 0, 0, 0
    
    math1 = [1, 2, 3, 4, 5]
    math2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a = [0] * 3
    
    for i in answers:
        if math1[i1] == i:
            a[0] += 1
            
        if math2[i2] == i:
            a[1] += 1
            
        if math3[i3] == i:
            a[2] += 1
            
        i1 = (i1 + 1) % len(math1)
        i2 = (i2 + 1) % len(math2)
        i3 = (i3 + 1) % len(math3)
        
    
    max_a = max(a)
    for i in range(3):
        if max_a == a[i]:
            answer.append(i+1)
            
    
    return answer