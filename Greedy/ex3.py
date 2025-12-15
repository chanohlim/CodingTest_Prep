'''
Greedy.ex3의 Docstring

입력:
3 3
3 1 2
4 1 4
2 2 2

출력:
2


n, m = map(int, input().split())
matrix = list()
mini = list()


for i in range(n):
    matrix.append(list(map(int,input().split())))

for vector in matrix:
    minimum = vector[0]
    for i in vector:
        if i <= minimum:
            minimum = i
    mini.append(minimum)

print(mini)
    
maxi = mini[0]
for i in mini:
    if i >= maxi:
        maxi = i

print(maxi)

'''

# 파이썬 기본 제공 함수인 min(), max() 함수를 사용해도 됨.

n, m = map(int, input().split())

result = 0

for i in range(n):

    data = list(map(int, input().split()))
    minimum = min(data)

    result = max(result, minimum)

print(result)