def solution(n, costs):
    answer = 0
    
    root = [i for i in range(n+1)]
    rank = [0 for i in range(n+1)]
    
    costs.sort(key=lambda x: x[2])
    
    for cost in costs:
        a, b, c = cost
        
        if union_by_rank(a, b, root, rank):
            answer += c
            
        
    return answer

def find_root(x, root):
    if x != root[x]:
        root[x] = find_root(root[x], root)
    
    return root[x]

def union_by_rank(a, b, root, rank):
    
    root_a = find_root(a, root)
    root_b = find_root(b, root)
    
    if root_a == root_b:
        return False
    
    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_b] > rank[root_a]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1
        
    return True