def solution(number, k):
    digit = len(number) - k
    number = list(map(str,number))
    
    start = 0
    
    while k > 0:
        print(number, start, len(number) - digit + 1)
        max_n = max(number[start:len(number) - digit + 1])
        
        for i in range(start, len(number)):
            if number[i] == max_n:
                break
        
        number = number[:start] + number[i:]
        
        k -= i - start
        start += 1

        print(k, start)
        
        digit -= 1

    print(''.join(number))
        
        
solution('1231234', 3)