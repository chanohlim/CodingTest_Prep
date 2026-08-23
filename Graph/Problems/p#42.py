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

root = [i for i in range(G + 1)]

def find_root(x):

    while x != root[x]:
        root[x] = root[root[x]]
        x = root[x]

    return x


def union(a, b):

    if a < b:
        root[b] = a
    else:
        root[a] = b


planes = []
cnt = 0

for p in range(P):
    planes.append(int(input()))


for p in planes:
    root_p = find_root(p)

    if root_p == 0:
        break

    union(root_p, root_p - 1)
    cnt += 1

print(cnt)