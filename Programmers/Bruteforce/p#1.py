def solution(sizes):
    answer = 0
    
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
    
    max_w = 0
    max_h = 0
    
    for size in sizes:
        if size[0] > max_w:
            max_w = size[0]
        
        if size[1] > max_h:
            max_h = size[1]
        
    return max_w * max_h
