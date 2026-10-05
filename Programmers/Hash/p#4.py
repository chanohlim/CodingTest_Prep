def solution(clothes):
    answer = 1
    
    data = dict()
    type = set()
    
    for value, key in clothes:
        data.setdefault(key, []).append(value)
        type.add(key)
    
    for key in type:
        answer *= len(data[key]) + 1
        
    return answer - 1