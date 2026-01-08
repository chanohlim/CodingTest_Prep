
N = int(input())
parts = list(map(int, input().split()))

M = int(input())
search = list(map(int, input().split()))

count = [0] * 1000001

for i in parts:
    count[i] += 1

for i in search:

    if count[i]:
        print("yes", end = ' ')
        
    else:
        print("no", end = ' ')