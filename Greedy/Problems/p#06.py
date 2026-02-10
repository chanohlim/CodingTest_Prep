import heapq

def solution(food_times, k):
    
    
    if k >= sum(food_times):
        return -1

    pq = list()

    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i+1))

    previous = 0
    length = len(food_times)

    while (pq[0][0] - previous) * length <= k:

        now = heapq.heappop(pq)[0]
        print(k)
        k -= (now - previous) * length
        print(k)
        length -= 1

        previous = now
        

    result = sorted(pq, key = lambda x: x[1])

    return result[k%length][1]


food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))
