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

N = int(input())

arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -(int(1e9))
min_val = int(1e9)

answer = []
operator = []

operator += [0] * add
operator += [1] * sub
operator += [2] * mul
operator += [3] * div

visited = [False] * len(operator)

def backtracking_1(i, now, add, sub, mul, div):

    global max_val, min_val

    if i == len(arr) - 1:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
        return

    else:

        if add > 0:
            backtracking_1(i + 1, now + arr[i + 1], add - 1, sub, mul, div)

        if sub > 0:
            backtracking_1(i + 1, now - arr[i + 1], add, sub - 1, mul, div)

        if mul > 0:
            backtracking_1(i + 1, now * arr[i + 1], add, sub, mul - 1, div)

        if div > 0:
            backtracking_1(i + 1, int(now / arr[i + 1]), add, sub, mul, div - 1)


def op(i, a, b):

    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    elif i == 3:
        return int(a / b)

def backtracking_2(now, length):

    if length == len(operator):
        answer.append(now)
        return
    
    for i in range(len(operator)):

        if visited[i]:
            continue

        if operator[i] == operator[i-1] and not visited[i-1]:
            continue

        visited[i] = True
        new = op(operator[i], now, arr[length + 1])

        backtracking_2(new, length + 1)

        visited[i] = False


backtracking_1(0, arr[0], add, sub, mul, div)
print(max_val, min_val)
backtracking_2(arr[0], 0)
print(max(answer), min(answer))