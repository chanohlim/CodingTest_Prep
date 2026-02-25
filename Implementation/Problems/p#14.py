'''

p#14 외벽 점검

입출력 예
n	weak	             dist	        result
12	[1, 5, 6, 10]	    [1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	    1


''' 

n = 12
weak1 = [1, 5, 6, 10]
dist1 = [1, 2, 3, 4]

weak2 = [1, 3, 4, 9, 10]
dist2 = [3, 5, 7]

def check(arr):

    for i in arr:
        if i == -1:
            return False
        
    return True


def clockwise(arr, start, dist):

    i = start
    n = len(arr)
    cnt = 0

    while dist > 0:

        print(i, dist)

        if arr[i] == -1:
            cnt += 1

        i += 1
        dist -= 1

        if i >= n:
            i = 0

    return cnt

def clock_change(arr, start, dist):

    i = start
    n = len(arr)

    while dist > 0:

        if arr[i] == -1:
            arr[i] = 0

        i += 1
        dist -= 1

        if i >= n:
            i = 0

def counterclock(arr, start, dist):

    i = start
    n = len(arr)
    cnt = 0

    while dist > 0:

        print(i, dist)

        if arr[i] == -1:
            cnt += 1

        i -= 1
        dist -= 1

        if i == -1:
            i = n-1

    return cnt

def counter_change(arr, start, dist):

    i = start
    n = len(arr)

    while dist > 0:

        if arr[i] == -1:
            arr[i] = 0

        i += 1
        dist -= 1

        if i == -1:
            i = n-1


def solution(n, weak, dist):

    answer = 0

    restaurant = [0] * n

    for i in weak:
        restaurant[i] = -1

    print(restaurant)

    dist.sort(reverse = True)

    for friend in dist:

        result = 0
        max_start = 0
        counter = False

        for i in weak:

            clock = clockwise(restaurant, i, friend)
            counter = counterclock(restaurant, i, friend)
            print('max:', clock, counter)

            if clock > counter:
                if clock > result:
                    result = clock
                    max_start = i
                    counter = False

            else:
                if counter > result:
                    result = counter
                    max_start = i
                    counter = True

        if counter:
            counter_change(restaurant, max_start, friend)
            print(friend, ':', end = ' ')
            print(restaurant)
        else:
            clock_change(restaurant, max_start, friend)
            print(friend, ':', end = ' ')
            print(restaurant)
        
        answer += 1

        if check(restaurant):
            break


    for i in restaurant:
        if i == -1:
            return -1
    
    return answer

print(solution(n, weak1, dist1))