from functools import cmp_to_key

def solution1(numbers):
    
    numbers = list(map(str, numbers))
    
    def compare(a, b):
        
        if a + b < b + a:
            return 1
        elif a + b > b + a:
            return -1
        
        return 0
    
    
    numbers.sort(key = cmp_to_key(compare))
    if numbers[0] == '0':
        return '0'
    
    answer = ''.join(numbers)
    
    
    return answer


def solution2(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(reverse = True, key = lambda x: x*3)
    
    
    if numbers[0] == '0':
        return '0'
    
    answer = ''.join(numbers)
    return answer