# 해시 카테고리의 문제라는 점에서 훨씬 우월한 솔루션이다.

def solution(participant, completion):
    
    dic = {}
    
    for p in participant:
        
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
            
    for c in completion:
        
        dic[c] -= 1
        
    for key in dic.keys():
        if dic[key] > 0:
            return key