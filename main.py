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

'''

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

teachers = []
answer = False

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i, j))


def radar():

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for teacher in teachers:
        i, j = teacher
        for k in range(4):

            di, dj = i + direction[k][0], j + direction[k][1]
            if 


def backtracking(a, b, length, N):
    global answer

    if length == 3:
        answer = answer or radar()

    for i in range(a, N):
        for j in range(b, N):
            graph[i][j] = 'O'
            backtracking(i)