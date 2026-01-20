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

graph = [[] for i in range(N + 1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a 노드에서 b 노드까지의 거리가 c


table = [[INF] * (N + 1) for i in range(N + 1)]

for i in range(N):
    table[i+1][i+1] = 0

for i in range(1, N + 1):
    for node in graph[i]:
        table[i][node[0]] = node[1]

for k in range(N): # k가 가장 밖에 있어야 이론적으로, 기능적으로도 맞는 플로이드-워셜 알고리즘. 1번부터 단계적으로 사용 가능한 노드 추가, 이래야 결국 마지막에 모든 경로의 가능한 수가 '흡수'됨
    for a in range(N):
        for b in range(N):
            table[a+1][b+1] = min(table[a+1][b+1], table[a+1][k+1] + table[k+1][b+1])


for i in range(N):
    for j in range(N):
        if table[i+1][j+1] == INF:
            print('INF', end = ' ')
        else:
            print(table[i+1][j+1], end = ' ')
    print()