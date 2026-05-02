'''

8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

9 - 0
7 - 1

'''
from sys import stdin
input = stdin.readline


N = int(input())

paper = []
answer = [0, 0]
movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    paper.append(list(map(int, input().split())))

def search(N, i, j):

    color = paper[i][j]

    origin_i = i
    origin_j = j


    for i in range(N):
        for j in range(N):

            if paper[origin_i + i][origin_j + j] != color: # 이 색종이가 전부 하나의 색이 아니면
                search(N//2, origin_i, origin_j) # 1사분면
                search(N//2, origin_i + N//2, origin_j) # 3사분면
                search(N//2, origin_i, origin_j + N//2) # 2사분면
                search(N//2, origin_i + N//2, origin_j + N//2) # 4사분면
                return
        
        
    answer[color] += 1
    return

search(N, 0, 0)

for i in answer:
    print(i)



