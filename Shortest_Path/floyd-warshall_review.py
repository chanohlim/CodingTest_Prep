'''

플로이드-워셜 알고리즘: 특정 노드에서 모든 노드까지의 최단 거리를 계산하는 알고리즘

1. 먼저 연결되어있는 간선 정보를 전부 2차원 배열에 넣는다.
2. 1번 노드부터 시작해서 각 노드를 거쳐간다고 생각하고, 그 노드를 제외한 모든 노드에서 2개를 선택해서 거리 계산
3. 마지막 노드까지 반복
4. 각 노드에서 모든 노드까지의 모든 최단 거리가 전부 계산된다.

a -> b 까지의 최단 거리를 각 노드마다 전부 계산할 때,
a 와 b 사이에 들어갈 수 있는 노드들이 점점 허용된다.

a -> 1 -> b
a -> 1 -> 2 -> b 등등

모든 경로는 a -> ... -> b 의 형태를 띄고,
...에 모든 경우가 들어가므로, 중간 노드로 1..k까지 허용하는 경우를 모두 고려하게 된다.
어떤 경로든, 그 중간 노드에는 최댓값 k가 존재한다.

a → (1,2,...,k-1 중 아무거나) → k → (1,2,...,k-1 중 아무거나) → b

k = 1  → 중간 노드 {1}
k = 2  → 중간 노드 {1,2}
k = 3  → 중간 노드 {1,2,3}



입력:
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력:
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''

N = int(input()) # 노드 수
E = int(input()) # 간선의 개수

INF = int(1e9)

table = [[INF] * (N + 1) for i in range(N + 1)]

for i in range(E):
    a, b, c = map(int, input().split())
    table[a][b] = min(table[a][b], c)

for i in range(1, N+1):
    table[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        print(table[i][j], end = ' ')
    print()
