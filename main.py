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

root = [i for i in range(N + 1)]
rank = [1 for i in range(N + 1)]

def find_root(x):

    while x != root[x]:
        root[x] = root[root[x]]
        x = root[x]

    return x


def union_by_rank(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b: # 사이클 발생
        return False

    if rank[root_a] < rank[root_b]:
        root[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    else:
        root[root_b] = root_a
        rank[root_a] += 1

    return True


data_x = []
data_y = []
data_z = []


for i in range(N):

    x, y, z = map(int, input().split())
    data_x.append((x, i+1))
    data_y.append((y, i+1))
    data_z.append((z, i+1))


data_x.sort(key=lambda x: x[0])
data_y.sort(key=lambda x: x[0])
data_z.sort(key=lambda x: x[0])

edges = []

for i in range(N-1):

    x1, a1 = data_x[i]
    x2, a2 = data_x[i+1]
    cost_x = abs(x1 - x2)

    y1, b1 = data_y[i]
    y2, b2 = data_y[i+1]
    cost_y = abs(y1 - y2)

    z1, c1 = data_z[i]
    z2, c2 = data_z[i+1]
    cost_z = abs(z1 - z2)

    edges.append((a1, a2, cost_x))
    edges.append((b1, b2, cost_y))
    edges.append((c1, c2, cost_z))


edges.sort(key = lambda x: x[2])

total = 0

for e in edges:

    a, b, cost = e

    possible = union_by_rank(a, b)

    if possible:
        total += cost

print(total)