'''

여러 노드가 있을 때, 특정 노드에서 각각의 노드로 가는 최단 거리를 구해주는 알고리즘
음의 간선이 없을 때만 정상 작동 => 음의 간선이 있을 시 벨만-포드 알고리즘 사용

하나의 노드를 선택해서 연결되어있는 간선들까지의 거리를 모두 계산하고 나면, 선택된 노드의 최단 거리는 확정된다.

이유:
1. 먼저, 시작 노드에서 각각의 노드로 가는 최단 거리(의 추정치)는 노드를 선택할 때마다 업데이트 된다.
2. 시작 노드에서 가까운 노드 순으로 선택해서 최단 거리를 비교하는 알고리즘이 실행된다.
3. 해당 노드가 처음 선택되면, 그 노드는 시작 노드에서 가장 가까운 노드라는 뜻이다.
   만약 다른 노드를 거쳐서 간다면, 그 노드는 처음 선택된 수가 없으므로 모순.
   만약 그 노드를 걸쳐서 다른 노드를 거쳤다가 다시 온다고 가정하면, 음의 간선이 없으므로 무조건 현재의 거릿값보다 큼. 모순.
   따라서, 해당 노드가 선택되는 순간부터 그 노드의 최단거리는 현재 값으로 고정이 되는 것이다.
4. 다음 노드가 선택되면, 그 노드는 이미 지난 노드(들)로 인해 최단거리가 갱신이 된 상태이므로,
   이전 노드(들)를 거쳐서 가는거랑 바로 가는거랑 이미 비교가 완료된 상태이다.
   따라서, 위와 같은 이유들로 인해 노드가 비교를 위해 선택이 되는 순간, 최단거리가 보장된다.
5. 마지막 노드가 선택되면, 이미 그 노드는 다른 노드를 방문하면서 갱신이 전부 완료된 상태이다.
   다른 노드를 거쳐서 가는 모든 경우의 수가 고려가 된 상태이므로, 이미 최솟값이다.
   그 노드를 거치고, 또다른 노드를 거쳤다가 다시 오는 경우는 무조건 현재 값보다 크므로 배제.
   따라서, 마지막 노드는 연결된 간선들을 확인할 필요가 없다.


입력:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2


출력:
0
2
3
1
2
4

'''

INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for i in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for i in range(E):
   a, b, c = map(int, input().split()) # a에서 b로 가는 비용이 c
   graph[a].append((b,c))


def smallest_node():

   index = -1
   min_val = INF
   for i in range(1, V+1):
      if (distance[i] < min_val) and not visited[i]:
         min_val = distance[i]
         index = i

   return index


def dijkstra(start):

   distance[start] = 0
   visited[start] = True

   for node in graph[start]:
      distance[node[0]] = min((distance[node[0]]), (distance[start] + node[1]))

   for i in range(V-1):
      now = smallest_node()
      
      if now == -1:
         break

      visited[now] = True

      for node in graph[now]:
         distance[node[0]] = min(distance[node[0]], distance[now] + node[1])


dijkstra(start)
print(distance)
         