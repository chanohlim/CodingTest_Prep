
def solution(n, computers):
    
    root = [i for i in range(n)]
    rank = [1 for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j, root, rank)

    for i in range(n):
        find_root(i, root)
        
    return len(set(root))


def find_root(x, root):
    if x != root[x]:
        root[x] = find_root(root[x], root)
        
    return root[x]

def union(a, b, root, rank):
    
    root_a = find_root(a, root)
    root_b = find_root(b, root)
    
    if root_a == root_b:
        return
    
    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_b] > rank[root_a]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1