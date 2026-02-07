'''

팀 결성)

처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N+1개의 팀이 존재. => 서로소 집합
선생님은 '팀 합치기'와 '같은 팀 여부 확인' 연산 가능 => union과 find_root

입력 조건:
N M
팀 합치기 => 0 a b
같은 팀 여부 확인 => 1 a b

a, b는 N 이하의 자연수


출력 조건:
'같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력


입력 예시:
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력 예시:
NO
NO
YES

'''

N, M = map(int, input().split())

root = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]

def find_root(node):
    if root[node] != node:
        root[node] = find_root(root[node])
    
    return root[node]

    
def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a == root_b:
        return
 
    if rank[root_a] > rank[root_b]:
        root[root_b] = root_a
    elif rank[root_b] > rank[root_a]:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
        rank[root_a] += 1

for i in range(M):
    
    selection, a, b = map(int, input().split())

    if selection == 0:
        union(a,b)
    else:
        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            print("YES")
        else:
            print("NO")

print(root)