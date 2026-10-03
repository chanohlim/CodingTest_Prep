from itertools import permutations
answer = -1

def solution(k, dungeons):
    global answer
    
    backtracking(k, dungeons, 0, len(dungeons))
    return answer


def backtracking(k, dungeons, length, n):
    global answer
    
    if length == n: # list empty
        answer = max(answer, length)
        print(answer)
        return
            
    for i in range(len(dungeons)):

        if k < dungeons[i][0]:
            answer = max(answer, length)
            continue
            
        backtracking(k - dungeons[i][1], dungeons[:i] + dungeons[i+1:], length + 1, n)

