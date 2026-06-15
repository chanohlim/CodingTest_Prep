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
add, sub, mul, div = map(int, input().split()) # + - x /

max_val = -(int(1e9))
min_val = int(1e9)
n = len(arr)
    

def backtracking(i, num):

    global max_val, min_val, add, sub, mul, div, n

    if i == n-1:
        print(num)
        max_val = max(max_val, num)
        min_val = min(min_val, num)
    else:

        if add > 0:
            add -= 1
            backtracking(i + 1, num + arr[i+1])
            add += 1
        
        if sub > 0:
            sub -= 1
            backtracking(i + 1, num - arr[i+1])
            sub += 1
        
        if mul > 0:
            mul -= 1
            backtracking(i + 1, num * arr[i+1])
            mul += 1

        if div > 0:
            div -= 1
            backtracking(i + 1, num // arr[i+1])

        

backtracking(0, arr[0])
print(max_val, min_val)

