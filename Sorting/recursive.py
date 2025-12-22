'''
Sorting.recursive의 Docstring

재귀 함수: 자기 자신을 다시 호출하는 함수

'''


def recursive(i):
    
    if i == 100:
        return
    
    print(i,'번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive(i+1)
    print(i,'번째 재귀 함수를 호출합니다.')

recursive(1)