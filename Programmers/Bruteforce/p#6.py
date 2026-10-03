from collections import deque

def solution(n, wires):
    answer = int(1e9)
    
    graph = [[] for i in range(n+1)]
    
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
        
    for wire in wires:
        
        a, b = wire
        
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(answer, bfs(n, 1, graph))
        
        graph[a].append(b)
        graph[b].append(a)    
        
    return answer


def bfs(n, start, graph):
    
    visited = [False] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
            
        for node in graph[now]:
            
            if not visited[node]:
                q.append(node)
                visited[node] = True

    
    cnt = 0
    for i in range(1, n+1):
        if visited[i]:
            cnt += 1
        
            
    return abs(n- 2*cnt)
            