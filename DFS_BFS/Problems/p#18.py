'''

p	        result
"(()())()"	"(()())()"
")("	    "()"
"()))((()"	"()(())()"


'''


def seperate(p):

    a = 0
    b = 0

    if p[0] == '(':
        a += 1
    else: # ')'
        b += 1

    i = 1

    while a != b:
        
        if p[i] == '(':
            a += 1
        else: # ')'
            b += 1

        i += 1

    return (p[:i], p[i:])
        

def correct(p):


    if p[0] == ')':
        return False
    


    a = 0
    b = 0

    for i in p:
        if i == '(':
            a += 1
        else:
            b += 1

        if b > a:
            return False

    return True

def reverse(p):

    temp = ""

    for i in p:
        if i == '(':
            temp += ')'
        else:
            temp += '('

    return temp


def solution(p):


    answer = ""


    if not p: # 1. 입력이 빈 문자열일 경우, 빈 문자열을 반환합니다.
        return ""

    u, v = seperate(p) # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리

    if correct(u):
        answer += ( u + solution(v))
    else:
        answer += ( '(' + solution(v) + ')' + reverse(u[1:-1]) )


    return answer

