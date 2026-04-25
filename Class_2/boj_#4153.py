'''

6 8 10
25 52 60
5 12 13
0 0 0


right
wrong
right


'''

arr = list(map(int, input().split()))

while arr[0] != 0:

    arr.sort()
    a, b, c = arr

    if (a*a) + (b*b) == (c*c):
        print("right")
    else:
        print("wrong")
    
    arr = list(map(int, input().split()))