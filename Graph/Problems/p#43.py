'''

7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

'''

N, M = map(int, input().split())

root = [i for i in range(N)]
rank = [0 for i in range(N)]

def find_root(node):

    while root[node] != node:
        root[node] = root[root[node]]
        node = root[node]
    
    return root[node]

def union(a, b):
    
    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b: # 사이클 발생
        return False
    
    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_a] < rank[root_b]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1

    return True

edges = []

for i in range(M):
    X, Y, Z = map(int, input().split())
    edges.append((X, Y, Z))

edges.sort(key = lambda x: x[2])

result = 0
cost = 0

for edge in edges:

    cost += edge[2]

    if union(edge[0], edge[1]):
        result += edge[2]

print(cost - result)