'''

그래프를 직접 만들기보단, 좌표 및 형태를 넣고, 모든 구조물에 대해 가능한지 여부 따져보고, 불가능하면 실행 취소

조건이 복잡하면, 국소적 수정보다 전체 검증이 더 안전하다.

'''


n = 5
build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
build_frame = [
    [0,0,0,1],
    [1,0,0,1],
    [2,0,0,1],
    [3,0,0,1],

    [0,1,1,1],
    [1,1,1,1],
    [2,1,1,1],

    [1,1,0,1],  # 위에 기둥 세우기
    [2,1,0,1],  # 위에 기둥 세우기

    [1,0,0,0]   # 아래 기둥 삭제
]

def possible(answer):

    for x, y, a in answer:

        if a == 0: # 기둥일 때
            if ( # 가능 조건
                (y == 0) or 
                ( (x - 1, y, 1) in answer) or 
                ( (x, y - 1, 0) in answer) or
                ( (x, y, 1) in answer)): # 기둥이 바닥 위에 있거나, 보 위에 있거나, 기둥 위에 있으면
                continue
        
        elif a == 1: # 보일 때
            if ( # 가능 조건
                ( (x, y - 1, 0) in answer) or 
                ( (x + 1, y - 1, 0) in answer) or 
                (( (x - 1, y, 1) in answer) and ( (x + 1, y, 1) in answer))):
                continue

        return False # 모두 해당 안되면 즉시 False 반환

    return True # 모두 통과했다면 True 반환 => 마지막 반복에서 continue가 되면 즉시 for문에서 탈출한다.
    

'''
def search(x, y, a, answer):


    for i in range(len(answer)):

        if answer[i] == [x, y, a]:
            return i
'''



def solution(n, build_frame):
    
    answer = set()

    for x, y, a, b in build_frame:
        
        if b == 1: # 설치 명령
            answer.add((x, y, a))
            if possible(answer):
                continue
            else:
                answer.remove((x, y, a))

        elif b == 0: # 삭제 명령
            #index = search(x, y, a, answer)
            answer.remove((x, y, a))
            if possible(answer):
                continue
            else:
                answer.add((x, y, a))
            

    return sorted(answer, key = lambda x: (x[0],x[1],x[2]))

print(solution(n, build_frame))