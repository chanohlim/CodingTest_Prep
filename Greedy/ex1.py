coins = [500,100,50,10]

n = int(input())
change = 0


for coin in coins:
    change += n // coin
    n %= coin

print(change)