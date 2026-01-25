'''

서로소 집합은 무방향 그래프 내에서 사이클을 판별할 때 사용할 수 있음

'''

V, E = map(int, input().split())

parent = [i for i in range(V + 1)]


def find_parent(parent, node):
    
    if parent[node] != node: # 자기 자신이 루트 노드가 아닐 때
        parent[node] = find_parent(parent, parent[node]) # 경로 압축 => return find_parent()에서 직접 parent[node]값을 바꾸어준다
    
    return parent[node] # 루트 노드를 반환

def union(parent, a, b):
    
    parent_a = find_parent(parent, a) # a의 루트
    parent_b = find_parent(parent, b) # b의 루트

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    
    else:
        parent[parent_a] = parent_b
    
cycle = False

for i in range(E):

    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union(parent, a, b)



print("싸이클 발생 여부:", cycle)