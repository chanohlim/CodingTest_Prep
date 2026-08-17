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

graph = []

root = [i for i in range(N + 1)]
rank = [1] * (N + 1)

for i in range(N):
    graph.append(list(map(int, input().split())))

def find_root(a):

    while root[a] != a:
        root[a] = root[root[a]]
        a = root[a]

    return a


def union_by_rank(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b: # root가 같으면 union 연산 불필요
        return

    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_a] < rank[root_b]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_by_rank(i+1, j+1)


plan = list(map(int, input().split()))
possible = True

for i in range(M-1):
    if find_root(plan[i]) != find_root(plan[i + 1]):
        possible = False

if possible:
    print("YES")
else:
    print("NO")