'''

크루스칼 알고리즘: 무방향 그래프에서 최소 신장 트리를 만드는 알고리즘

서로소 집합 자료구조가 사용되고, 그리디 알고리즘이다.(간선이 최소인 것부터 탐색 시작)

1. 간선을 오름차순으로(최솟값이 가장 앞으로 가게) 정렬한다.
2. 두 개의 노드의 루트 노드를 비교한다.
3. 만약 두 노드의 루트 노드가 동일하지 않다면(사이클이 발생하지 않는다면) 두 노드를 union 연산한다.
4. 모든 간선들을 탐색할 때까지 반복

1 2 3 4 5 6 7

1 2 3 4 5 6 7         
1 2 3 3 5 6 7
1 2 3 3 5 6 3
1 2 3 3 5 3 3
1 2 3 3 5 3 3 X
1 1 3 3 5 3 3 => 오류 발생, 6의 parent node만 바꾸고, 6의 루트 노드를 바꾸지 않았다. 6의 root인 3의 parent를 1로 변경해야됨
1 1 3 3 5 1 3 (오류) => 1 1 1 3 5 3 3 => 6은 그대로 3을 가르키고, 3의 부모(루트) 노드는 1이 되었다. 즉, 3의 집합과 1의 집합이 합집합이 된 것.



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

def find_root(root, node):
    
    if root[node] != node:
        root[node] = find_root(root, root[node])
    
    return root[node]


def union(root, a, b):

    root_a = find_root(root, a) # a의 루트 노드
    root_b = find_root(root, b) # b의 루트 노드

    if root_a < root_b:
        root[root_b] = root_a # b의 루트 노드의 부모 = a의 루트 노드 값
    else: # 만약 parent[b] = parent_a 이면, 논리적으로 b(루트 노드임이 보장이 안됨)의 부모가 노드 a의 루트 값이 되는거니, 집합 전체를 합치는게 아니다.
        root[root_a] = root_b # a의 루트 노드의 부모 = b의 루트 노드 값


V, E = map(int, input().split())

edges = list()

for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


root = [i for i in range(V + 1)]

edges.sort()

total = 0

for edge in edges: print(edge)

for edge in edges:
    
    root_a = find_root(root,edge[1])
    root_b = find_root(root,edge[2])

    if root_a == root_b: # 사이클 발생 시
        print(f'{edge[1]}, {edge[2]} 의 루트 노드가 {root_a}로 동일! 사이클 발생, total: {total}')
        continue

    total += edge[0]
    union(root, edge[1], edge[2])
    print(f'{edge[1]}: {root_a}, {edge[2]}: {root_b}')
    print("total:",total-edge[0],"+",edge[0])


print(total)