'''

4
3
4
1
1

2

4
6
2
2
3
3
4
4

3

'''
from sys import stdin
input = stdin.readline

G = int(input())
P = int(input())

root = [i for i in range(G+1)]

def find_root(x):

    while root[x] != x:
        root[x] = root[root[x]]
        x = root[x]
    
    return x

def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b:
        return

    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b

planes = []
cnt = 0

for i in range(P):
    planes.append(int(input()))

for p in planes:
    root_plane = find_root(p)

    if root_plane == 0:
        break
    else:
        union(root_plane, root_plane - 1) # 도킹
        cnt += 1

print(cnt)