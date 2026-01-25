'''

서로소 집합: 공통 원소가 없는 두 집합

서로소 집합 연산: union(합집합), find(찾기)


입력 예시:
6 4
1 4
2 3
2 4
5 6


출력 예시:
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5

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
    

for i in range(E):

    a, b = map(int, input().split())
    union(parent, a, b)




print('각 원소가 속한 집합: ', end = '')
for i in range(1, V + 1):
    print(find_parent(parent, i), end= ' ')

print()

print('부모 테이블: ', end = '')
for i in range(1, V + 1):
    print(parent[i], end = ' ')

print()