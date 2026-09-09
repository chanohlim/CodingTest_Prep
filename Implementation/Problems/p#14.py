'''

p#14 외벽 점검

입출력 예
n	weak	             dist	        result
12	[1, 5, 6, 10]	    [1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	    1


''' 

n = 12
weak1 = [1, 5, 6, 10]
dist1 = [1, 2, 3, 4]

weak2 = [1, 3, 4, 9, 10]
dist2 = [3, 5, 7]


from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    
    length = len(weak)
    
    for i in range(length):
        weak.append(n + weak[i])
        
        
    for friend in permutations(dist, len(dist)):
        
        for start in range(length):
            
            cnt = 1
            position = weak[start] + friend[cnt - 1]
            possible = True
            
            for idx in range(start + 1, start + length):
                
                if position < weak[idx]:
                    
                    cnt += 1
                    if cnt > len(dist):
                        break
                        
                    position = weak[idx] + friend[cnt - 1]
                    
            answer = min(cnt, answer)

    if answer == len(dist) + 1:
        return -1
    
    return answer