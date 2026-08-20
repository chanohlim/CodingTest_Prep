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

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

road = []

root = [i for i in range(N + 1)]
rank = [1 for i in range(N + 1)]

total = 0

for i in range(M):
    x, y, z = map(int, input().split())
    road.append((x, y, z))
    total += z

road.sort(key=lambda x: x[2])

def find_root(x):

    while root[x] != x:
        root[x] = root[root[x]]
        x = root[x]
    
    return x

def union_by_rank(a, b):
    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b:
        return False

    
    if rank[root_a] < rank[root_b]:
        root[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    else:
        root[root_b] = root_a
        rank[root_a] += 1

    return True


cost = 0

for r in road:
    x, y, z = r
    possible = union_by_rank(x, y)

    if possible:
        cost += z

print(total - cost)