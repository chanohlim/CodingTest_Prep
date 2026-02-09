'''

#04 만들 수 없는 금액

입력 예시:
5
3 2 1 1 9

출력 예시:
8

'''

N = int(input())

coins = list(map(int, input().split()))
coins.sort()


target = 1
flag = True

for coin in coins:
    
    if coin > target:
        print(target)
        flag = False
        break
    target += coin 

if flag:
    print(target)

'''

bruteforce로 풀어봤는데 실패(시간초과)

N = int(input())

coins = list(map(int, input().split()))
coins.sort(reverse = True)

print(coins)

for i in range(1, sum(coins)+1):

    idx = 0
    result = 0

    if min(coins) > i:
        print(f"not able to make {i}")
        break

    while coins[idx] > i:
        idx += 1

    print(f'current:{i}, value[idx]:{coins[idx]},{idx} =>', end = ' ')

    for coin in coins[idx:]:
        
        if (result + coin) <= i:
            result += coin
            print(coin, end= ' ')
            if result == i:
                break

    print('=', result)

    print()
    
    if result != i:
        print(f"{result} - not able to make {i}")
        break


'''