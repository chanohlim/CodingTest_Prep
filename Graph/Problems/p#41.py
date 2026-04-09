'''

5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

YES

'''

N, M = map(int, input().split())

root = [i for i in range(N + 1)]
rank = [0 for i in range(N + 1)]

def find_root(node):

    if root[node] != node:
        root[node] = find_root(root[node])
    
    return root[node]

def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b:
        return

    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_a] < rank[root_b]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            union(i, j+1)

plan = list(map(int, input().split()))
flag = True

for i in range(M-1):
    
    a = plan[i]
    b = plan[i + 1]

    if find_root(a) != find_root(b):
        flag = False

if flag:
    print("YES")
else:
    print("NO")

