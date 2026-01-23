'''
최단경로
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	257809	82631	42980	27.274%
문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력:
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다.
(1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.


입력 예시:
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

출력 예시:
0
2
3
7
INF

'''

import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)

graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):

    pq = list()
    distance[start] = 0

    heapq.heappush(pq,(0, start))

    while pq:

        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for node in graph[now]:

            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0]))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
