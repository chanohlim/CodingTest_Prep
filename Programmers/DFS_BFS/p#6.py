def solution(tickets):
    answer = []
    
    visited = [False] * len(tickets)
    backtracking(["ICN"], tickets, visited, "ICN", answer)
    
    answer.sort()
    
    return answer[0]


def backtracking(path, tickets, visited, now, answer):
    
    if len(path) == len(tickets) + 1:
        answer.append(list(path))
        return
    
    for i in range(len(tickets)):
        
        if visited[i]:
            continue
            
        if tickets[i][0] == now:
            path.append(tickets[i][1])
            visited[i] = True
            backtracking(path, tickets, visited, tickets[i][1], answer)
            path.pop()
            visited[i] = False
            
        
    