'''

배워갈 점:
1. 조합으로 벽 세우기 후 완전탐색 => 백트래킹으로도 가능(두 번째 시도때 해보자)
2. dfs 대신 bfs로 해야지 재귀깊이 초과할 위험도 없고 더 빠르다. 어차피 그래프 완전탐색은 둘 다 똑같이 기능한다.
3. 2차원 배열 복사는 deepcopy보다, copy = [row[:] for row in graph] 로 하는게 더 빠르다.
4. bfs 하고 0을 일일히 카운트하기보다, bfs를 돌면서 확산되는 개수를 카운팅하고, 그걸 return 받아서 수식으로 계산하는게 훨씬 빠름

7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

9

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

3

7 7
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 1 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

'''
from collections import deque
from time import sleep
from sys import stdin
input = stdin.readline

def print_graph(arr):
    print()

    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()

    print()

# bfs로 바이러스 퍼트리기
def bfs(lab, viruses, N, M):
    cnt = 0

    q = deque(viruses)
    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:

        i, j = q.popleft()

        for k in range(4):
            di, dj = i + movement[k][0], j + movement[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue


            if lab[di][dj] == 0:
                lab[di][dj] = 2
                q.append((di, dj))
            else: # lab[di][dj] = 1 or 2 => 벽이거나 바이러스이므로 스킵
                continue

    
    #print_graph(lab)
    #sleep(1)

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                cnt += 1
            elif lab[i][j] == 2:
                lab[i][j] = 0
    
    for virus in viruses:
        i, j = virus
        lab[i][j] = 2
    
    return cnt 
    #return len(empty) - 3 - infected  => 원래 빈 공간에서 세운 벽 3개를 빼고, 새로 감염된 수(bfs 하면서 세기) 빼면 시간복잡도 최적화

N, M = map(int, input().split())

lab = []
empties = []
viruses = []

result = 0

for i in range(N):
    lab.append(list(map(int, input().split())))

# 빈칸, 바이러스 위치 구하기
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empties.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))


# 벽 세우기
def backtracking(start, length, N, M):
    global result

    if length == 3:
        #print_graph(lab)
        #sleep(1)
        result = max(result, bfs(lab, viruses, N, M))
        return

    
    for i in range(start, len(empties)):
        x, y = empties[i]
        lab[x][y] = 1 # 벽 세우기
        backtracking(i + 1, length + 1, N, M)
        lab[x][y] = 0 # 벽 지우기



# 반복 후 안전 영역의 최댓값 출력
backtracking(0, 0, N, M)
print(result)