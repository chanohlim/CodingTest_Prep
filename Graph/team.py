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
YES
YES

'''

N, M = map(int, input().split())

root = [i for i in range(N + 1)]


def find_root(node):

    if root[node] != node:
        root[node] = find_root(root[node])

    return root[node]


def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b


for i in range(M):

    task, a, b = map(int, input().split())


    if task == 0:
        union(a, b)

    elif task == 1:

        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            print('YES')
        else:
            print('NO')