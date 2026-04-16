'''

5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

4

'''
from sys import stdin
input = stdin.readline

N = int(input())

root = [i for i in range(N)]
rank = [0 for i in range(N)]
coor = []
edges = []

def find_root(node):
    
    while root[node] != node:
        root[node] = root[root[node]]
        node = root[node]

    return root[node]

def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b:
        return False
    
    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a

    elif rank[root_a] < rank[root_b]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1

    return True



for i in range(N):
    X, Y, Z = map(int, input().split())
    coor.append((X, Y, Z, i))

def cost(a, b, i):
    return abs(a[i] - b[i])



for i in range(3):
    coor.sort(key=lambda x: x[i])
    
    for j in range(N-1):
        edges.append((cost(coor[j], coor[j+1], i), coor[j][3], coor[j+1][3]))

edges.sort(key=lambda x: x[0])

result = 0

for edge in edges:
    if union(edge[1], edge[2]):
        result += edge[0]

print(result)