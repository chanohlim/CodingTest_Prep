'''

우선순위 큐(최소 힙으로 구현)를 사용한 다익스트라 알고리즘

'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9) # 10억

N, M = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input())

graph = [[] for i in range(N + 1)] # 인덱스 접근을 노드 값으로 할 예정
distance = [INF] * (N + 1)

# 모든 간선 정보 입력하기
for i in range(M):
    
    a, b, c = map(int, input().split()) 
    # a노드에서 b노드까지의 거리: c
    graph[a].append((b, c))


def dijkstra(start):
    
    pq = []

    heapq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq: # pq가 비어있지 않으면 계속 pop해서 거리 갱신
        
        dist, now = heapq.heappop(pq) # 우선순위 제일 높은(거리 제일 가까운) 루트 노드 pop (거리, 노드)
        
        if dist > distance[now]: # 이미 방문한 노드면 스킵 => 현재 노드까지의 최단거리보다 pop된 노드의 cost가 크면 이미 최솟값 확정된 방문 노드므로 스킵
            continue
        
        for node in graph[now]:

            cost = dist + node[1] # cost = 현재 노드까지의 최단거리 + 다음 노드까지의 거리

            if cost < distance[node[0]]: # 새로운 최솟값 등장 => 갱신
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0])) # 갱신된 distance 값 우선순위 큐에 push


dijkstra(start)

print(distance)
