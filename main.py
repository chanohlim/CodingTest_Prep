'''

예제 입력 1 
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
예제 출력 1 
5
예제 입력 2 
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
예제 출력 2 
10
예제 입력 3 
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
예제 출력 3 
11
예제 입력 4 
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
예제 출력 4 
32

'''
from sys import stdin
input = stdin.readline

import itertools

N, M = map(int, input().split())

city = []

for i in range(N):
    city.append(list(map(int, input().split())))

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))


def chicken_distance(house, chicken):

    result = 0
    
    for home in house:
        distance = int(1e9)

        for c in chicken:
            distance = min(distance, abs(home[0] - c[0]) + abs(home[1] - c[1]) )

        result += distance

    return result

answer = int(1e9)


def backtracking(start, path, M):

    global answer

    if len(path) == M:
        answer = min(answer, chicken_distance(house, list(path)))
        print(list(path))
        return


    for i in range(start, len(chicken)):
        x, y = chicken[i]
        path.append((x, y))
        backtracking(i+1, path, M)
        path.pop()
        

# backtracking(0, [], M)

for combination in itertools.combinations(chicken, M):

    answer = min(answer, chicken_distance(house, combination))

print(answer)