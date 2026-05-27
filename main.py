'''
key	lock	result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true
'''

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()

        
        
def solution(key, lock):
    answer = False
    
    M = len(key)
    N = len(lock)
    
    lock_extended = [[0] * (3 * N) for i in range(3*N)]

    # 확장된 행렬에 기존 lock 추가
    for i in range(N):
        for j in range(N):
            lock_extended[N+i][N+j] = lock[i][j]
        
    
    for a in range(4):
        
        for i in range(0, 2*N):
            for j in range(0, 2*N):

                for k in range(M):
                    for l in range(M):
                        lock_extended[i+k][j+l] += key[k][l]

                if check([lock_extended[i][N:2*N] for i in range(N, 2*N)]):
                    return True
                
                else:
                    for k in range(M):
                        for l in range(M):
                            lock_extended[i+k][j+l] -= key[k][l]

        key = rotate(key, M)
    
    
    
    return answer


def rotate(arr, M): # rotate 90 degrees clockwise
    
    new_arr = [[0] * M for i in range(M)]
    
    for i in range(M):
        for j in range(M):
            new_arr[i][j] = arr[M - j - 1][i]

    return new_arr
            
def check(arr):
    
    for i in arr:
        for j in i:
            if j != 1:
                return False
    
    return True


print(solution(key, lock))