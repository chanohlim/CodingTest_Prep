'''

크루스칼 알고리즘: 무방향 그래프에서 최소 신장 트리를 만드는 알고리즘

서로소 집합 자료구조가 사용되고, 그리디 알고리즘이다.(간선 비용이 최소인 것부터 탐색 시작)

1. 간선 비용을 오름차순으로(최솟값이 가장 앞으로 가게) 정렬한다.
2. 두 개의 노드의 루트 노드를 비교한다.
3. 만약 두 노드의 루트 노드가 동일하지 않다면(사이클이 발생하지 않는다면) 두 노드를 union 연산한다.
4. 모든 간선들을 탐색할 때까지 반복



입력:
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

출력:
159

'''

V, E = map(int, input().split())
edges = []

root = [i for i in range(V + 1)]
rank = [0 for i in range(V + 1)]

for i in range(E):

    a, b, cost = map(int, input().split())

    edges.append((cost, a, b))

edges.sort()

def find_root(node):
    if root[node] != node:
        root[node] = find_root(root[node])
    
    return root[node]

def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_b] > rank[root_a]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1

def cycle(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b:
        return True
    else:
        return False
    

def kruskal(edges):

    result = 0

    for edge in edges:
        cost, a, b = edge

        if cycle(a,b):
            continue

        union(a, b)
        result += cost

    return result


print(kruskal(edges))
