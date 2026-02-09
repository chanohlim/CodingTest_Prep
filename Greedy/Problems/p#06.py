def solution(food_times, k):
    
    
    if k >= sum(food_times):
        return -1
    
    ans_list = list()
    for i in range(len(food_times)):
        ans_list.append((food_times[i],i+1))

    ans_list.sort()
    
    answer = 0

    while k > 0:

        if k - ans_list[answer][0] < 0:
            break
        elif k == ans_list[answer][0]:
            answer += 1
            break

        k -= ans_list[answer][0]
        answer += 1

    answer = ans_list[answer][1]

    return answer

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))
