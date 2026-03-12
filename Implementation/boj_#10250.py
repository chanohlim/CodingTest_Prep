'''

문제: ACM 호텔

2
6 12 10
30 50 72

402
1203

'''

def room(H,N):

    room_number = N // H
    
    if N % H != 0:
        room_number += 1
        floor = N % H
    else:
        floor = H

    return (((floor) * 100) + room_number)

    


T = int(input())

answers = []

for i in range(T):

    H, W, N = map(int, input().split())
    answers.append(room(H, N))


for answer in answers:
    print(answer)
