'''

https://school.programmers.co.kr/learn/courses/30/lessons/468370

입출력 예
message	spoiler_ranges	result
"here is muzi here is a secret message"	[[0, 3], [23, 28]]	1
"my phone number is 01012345678 and may i have your phone number"	[[5, 5], [25, 28], [34, 40], [53, 59]]	4

'''

def solution(message, spoiler_ranges):
    answer = 0
    
    words = list(message.split())
    revealed = words[:]
    
    shown = set()
    
    for spoiler in spoiler_ranges:
        
        start = word_order(spoiler[0], message, True)
        end = word_order(spoiler[1] , message, False)
        
        for i in range(start, end+1):
            
            revealed[i] = 0
    
 
    for spoiler in spoiler_ranges:
        
        start = word_order(spoiler[0], message, True)
        end = word_order(spoiler[1] , message, False)
        
        for i in range(start, end+1):
            
            if words[i] in shown:
                continue
                
            flag = False
                
            for word in revealed:
                if word == words[i]:
                    flag = True
                    break
                    
            if flag:
                continue
                
            shown.add(words[i])
            answer += 1
            revealed[i] = words[i]
        
        
    return answer

def word_order(index, message, start):
    
    result = 0
    
    for i in range(index+1):
        if message[i] == ' ':
            result += 1
            
    if message[index] == ' ' and not start:
        result -= 1
    
            
    return result