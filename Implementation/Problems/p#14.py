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

from itertools import permutations

def solution(n, weak, dist):
    
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 초기화
    
    for start in range(length):

        for friends in list(permutations(dist, len(dist))):
            count = 1

            position = weak[start] + friends[count - 1] # 친구가 점검할 수 있는 마지막 위치

            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어난 경우
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)        

    if answer > len(dist):
        return -1
    return answer
