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

root = [i for i in range(N+1)]
rank = [1 for i in range(N+1)]

data_x = []
data_y = []
data_z = []

for i in range(N):
    x, y, z = map(int, input().split())

    data_x.append((x, i+1))
    data_y.append((y, i+1))
    data_z.append((z, i+1))


data_x.sort()
data_y.sort()
data_z.sort()

edges = []

for i in range(N - 1):
    x1, a1 = data_x[i]
    x2, a2 = data_x[i + 1]

    y1, b1 = data_y[i]
    y2, b2 = data_y[i + 1]

    z1, c1 = data_z[i]
    z2, c2 = data_z[i + 1]

    edges.append((a1, a2, x2-x1))
    edges.append((b1, b2, y2-y1))
    edges.append((c1, c2, z2-z1))

edges.sort(key=lambda x:x[2])


def find_root(x):

    while root[x] != x:
        root[x] = root[root[x]]
        x = root[x]

    return x


def union_by_rank(a, b):

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

total = 0

for e in edges:
    a, b, cost = e

    possible = union_by_rank(a, b)
    if possible:
        total += cost

print(total)