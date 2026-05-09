'''

https://school.programmers.co.kr/learn/courses/30/lessons/468371

출력 예

signals	
result

[[2, 1, 2], [5, 1, 1]]	
13

[[2, 3, 2], [3, 1, 3], [2, 1, 1]]	
11

[[3, 3, 3], [5, 4, 2], [2, 1, 2]]	
193

[[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]	
-1

'''
from functools import reduce

def gcd(a, b):

    while b != 0:
        r = a % b
        a = b
        b = r

    return a

def lcm(a, b):

    return (a * b) // gcd(a, b)

def solution(signals):

    cycles =  [ g + y + r for g, y, r in signals]

    limit = reduce(lcm, cycles)

    for t in range(1, limit + 1):
        ok = True

        for g, y, r in signals:
            cycle = g + y + r
            time = t % cycle

            if time == 0:
                time = cycle
            
            if not (g < time <= g + y):
                ok = False
                break
        
        if ok:
            return t
        
    return -1

