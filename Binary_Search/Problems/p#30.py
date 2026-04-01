def parametric(words, target, prefix, length):

    result = 0
    l = len(target)

    if prefix: # ?가 앞에 붙어있음
        for word in words:
            if word[-l:] == target and len(word) == length:
                result += 1
            

    else: # ?가 뒤에 붙어있음
        for word in words:
            if word[:l] == target and len(word) == length:
                result += 1

    return result


def solution(words, queries):
    answer = []
    prefix = False

    for query in queries:
        length = len(query)
        if query[0] == '?':
            prefix = True
        else:
            prefix = False
        
        target = query.strip('?')

        answer.append(parametric(words, target, prefix, length))


    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao", "prost"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# result = [3, 2, 4, 1, 0]

print(solution(words, queries))