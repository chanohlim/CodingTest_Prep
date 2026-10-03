answer = 0
found = False

def solution(word):
    global answer

    alphabet = ['A', 'E', 'I', 'O', 'U']
    backtracking('', 5, alphabet, word)
    
    return answer


def backtracking(path, n, alphabet, word):
    global answer, found
    
    if len(path) == n:
        return
        
    for i in range(len(alphabet)):
        
        path += alphabet[i]
        answer += 1
        
        if path == word:
            found = True
            return
        
        backtracking(path, n, alphabet, word)
        
        if found:
            return
        
        path = path[:-1]
        
        
        