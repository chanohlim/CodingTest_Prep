'''

#08 문자열 재정렬

입력:
K1KA5CB7

AJKDLSI412K4JSJ9D

출력:
ABCKK13

ADDIJJJKKLSS20

'''

s = input()

def ascii_cnt(s):

    answer = [0] * 91
    total = 0

    for i in s: # ascii 코드 값 65를 기준으로 알파벳과 숫자 구별
        
        code = ord(i)

        if code >= 65:
            answer[code] += 1
        else:
            total += int(i)

    for i in range(65, 91):
        
        if answer[i] == 0:
            continue

        for j in range(answer[i]):
            print(chr(i), end='')

    print(total)

def best(s):

    letters = []
    total = 0

    for i in s:

        if i.isalpha(): # 'A' <= i <= 'Z' 도 가능
            letters.append(i)
        else:
            total += int(i)
    
    letters.sort()
    
    for i in letters:
        print(i, end='')
    print(total)


ascii_cnt(s)
best(s)