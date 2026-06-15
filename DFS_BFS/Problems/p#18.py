def seperate(p):
    
    a = 0
    b = 0
    
    
    for i in range(len(p)):
        
        if p[i] == '(':
            a += 1
        elif p[i] == ')':
            b += 1
            
        if a == b:
            break
    
    
    u = p[:i+1]
    v = p[i+1:]
    
    return u, v

def correct(u):
    
    if not u:
        return True
    
    if u[0] == ')':
        return False
    
    count = 0
    
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        elif u[i] == ')':
            count -= 1
            
        if count < 0:
            return False
        
    return True

def reverse(p):
    
    a = ''
    
    for i in p:
        if i == '(':
            a += ')'
        elif i == ')':
            a += '('
            
    return a

def main(p):
    
    if p == '':
        return p
    
    u, v = seperate(p)
    
    if correct(u):
        return u + main(v)
    else:
        return '(' + main(v) + ')' + reverse(u[1:-1])
        

def solution1(p):
    
    if correct(p):
        return p
    
    answer = main(p)

    return answer

# 또는 main 함수를 solution 안에 넣어서 solution 자체가 재귀함수가 되도록 해도 된다.

def solution2(p):
    
    if correct(p):
        return p
    
    
    if p == '':
        return p
    
    u, v = seperate(p)
    
    if correct(u):
        return u + solution2(v)
    else:
        return '(' + solution2(v) + ')' + reverse(u[1:-1])