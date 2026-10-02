from math import sqrt

def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(sqrt(yellow)) + 1):
        if yellow % i == 0:
            j = yellow // i
            
            if ((2 * i) + (2 * j) + 4) == brown:
                answer.append(i+2)
                answer.append(j+2)
                break
    
    answer.sort(reverse = True)
    
    return answer