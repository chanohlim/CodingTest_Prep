def solution(phone_book):
    
    phone_book.sort()
    
    answer = True
    
    for i in range(len(phone_book) - 1):
        now = phone_book[i]
        next = phone_book[i+1]
        
        if now == next[:len(now)]:
            return False
    
    return answer