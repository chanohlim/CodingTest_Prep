'''

5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

YES

4
S S S T
X X X X
X X X X
T T T X

NO


2차원 배열에서 백트래킹 => 좌표들의 조합으로 구현하기

'''
from time import sleep

N = int(input())
graph = []
empties = []

answer = False # 모든 학생들이 감시를 피하는 경우의 수 존재
cnt = 0

for i in range(N):
    graph.append(list(input().split()))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
teachers = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i,j))
        elif graph[i][j] == 'X':
            empties.append((i,j))

def print_graph(graph):

    print()

    for i in graph:
        for j in i:
            print(j, end = ' ')
        print()

def track():

    for teacher in teachers:
        x, y = teacher

        for i in range(4):

            dx, dy = x + d[i][0], y + d[i][1]
            while (0 <= dx < N) and (0 <= dy < N):

                if graph[dx][dy] == 'O':
                    break
                
                if graph[dx][dy] == 'S':
                    return False

                dx, dy = dx + d[i][0], dy + d[i][1]

    return True # 한번도 학생이 발각이 안되었으면 True를 return
                


def backtracking(start, length):

    global answer

    if length == 3:
        answer = answer or track() # 한번이라도 감시 피하는게 가능한 경우가 있다면 True로 변한다.
        return
    
    for i in range(start, len(empties)):
        
        x, y = empties[i]

        graph[x][y] = 'O'
        backtracking(i + 1, length + 1)
        graph[x][y] = 'X'



backtracking(0, 0)

if answer: # 
    print("YES")
else:
    print("NO")