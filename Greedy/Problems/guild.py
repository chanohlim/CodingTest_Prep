'''

#01 모험가 길드


입력 예시:
5
2 3 1 2 2


출력 예시:
2

'''

N = int(input())
explorer = list(map(int, input().split()))

explorer.sort(reverse = True)

i = 0
result = 0


while i < len(explorer):

    i += explorer[i]
    result += 1

print(result)