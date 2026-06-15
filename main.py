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
    graph.append(list(input().split()))

teachers = []
answer = False

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i, j))

def print_arr(graph):
    print()

    for i in graph:
        for j in i:
            print(j, end = ' ')
        print()
    
    print()

def radar():

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for teacher in teachers:
        i, j = teacher
        for k in range(4):
            
            di, dj = i + direction[k][0], j + direction[k][1]

            while di >= 0 and di < N and dj >= 0 and dj < N:
                if graph[di][dj] == 'O':
                    break

                if graph[di][dj] == 'S':
                    return False

                di += direction[k][0]
                dj += direction[k][1]

    return True


def backtracking(start, length, N):
    global answer

    if answer:
        return

    if length == 3:
        answer = answer or radar()
        #print_arr(graph)
        return

    for i in range(start, N*N):
        a = i // N
        b = i % N

        if graph[a][b] != 'X':
            continue

        graph[a][b] = 'O'
        backtracking(i + 1, length + 1, N)
        graph[a][b] = 'X'
        

backtracking(0, 0, N)

if answer:
    print("YES")
else:
    print("NO")