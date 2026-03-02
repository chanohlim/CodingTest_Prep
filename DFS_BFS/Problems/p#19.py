'''

입력 예시 1
2
5 6
0 0 1 0

출력 예시 1
30
30

입력 예시 2
3
3 4 5
1 0 1 0

출력 예시 2
35 17

입력 예시 3
6
1 2 3 4 5 6
2 1 1 1

출력 예시 3
54
-24

'''

INF = int(1e9)

N = int(input())
A = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))

add, sub, mul, div = op_cnt
max_val = -(int(1e9))
min_val = int(1e9)

op = ['+', '-', '*', '//']
operator = []

for i in range(4):
    operator += [op[i]] * op_cnt[i]

visited = [False] * (N - 1)

answer = []

def ops(a, b, o):

    if o == '+':
        return (a + b)
    elif o == '-':
        return (a - b)
    elif o == '*':
        return (a * b)
    elif o == '//':
        if a < 0:
            return -((-a) // b)
        else:
            return (a // b)

def backtracking(result, length, visited): # 연산자 하나씩 방문하면서, 중복 순열을 만들고 거기서 바로 결과값을 도출해서 리스트에 append

    if length == len(operator):
        answer.append(result)
        return


    for i in range(len(operator)):

        if visited[i]:
            continue

        if i > 0 and operator[i] == operator[i-1] and not visited[i-1]: # 중복 순열 제거 코드
            continue


        new = ops(result, A[length + 1], operator[i])
        visited[i] = True
        backtracking(new, length+1, visited)


        visited[i] = False

def dfs(i, now): # 모든 operator를 다 쓸때까지 재귀적으로 함수 호출(dfs)해서 결과값 계산, 그 후 복원(백트래킹)

    global max_val, min_val, add, sub, mul, div

    if i == N:
        max_val = max(max_val, now)
        min_val = min(min_val, now)

    if add > 0:
        add -= 1
        dfs(i + 1, now + A[i])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(i + 1, now - A[i])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(i + 1, now * A[i])
        mul += 1

    if div > 0:
        div -= 1
        dfs(i + 1, int(now / A[i]))
        div += 1


# backtracking(A[0], 0, visited)
dfs(1, A[0])

print(max_val, min_val)