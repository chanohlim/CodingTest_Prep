from collections import deque

def solution(begin, target, words):
    global answer
    
    if target not in words:
        return 0
    
    answer = bfs(begin, target, words)            
    
    visited = [False] * len(words)
    answer = int(1e9)
    
    dfs(target, words, begin, 0, visited)
    
    return answer

def bfs(begin, target, words):
    
    visited = [False] * len(words)
    
    q = deque()
    q.append((0, begin))
    
    while q:
        dist, now = q.popleft()
        
        if now == target:
            return dist
        
        for i in range(len(words)):
            
            cnt = 0
            
            if visited[i]:
                continue
            
            for j in range(len(words[i])):
                if now[j] != words[i][j]:
                    cnt += 1
            
            if cnt == 1:
                q.append((dist + 1, words[i]))
                visited[i] = True
    
def dfs(target, words, now, count, visited):
    global answer
    
    if now == target:
        answer = min(answer, count)
        return
    
    for i in range(len(words)):
        word = words[i]
        cnt = 0
        
        if visited[i]:
            continue
            
        for idx in range(len(word)):
            if now[idx] != word[idx]:
                cnt += 1
                
        if cnt == 1:
            visited[i] = True
            dfs(target, words, word, count + 1, visited)
            visited[i] = False