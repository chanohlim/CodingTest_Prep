coin = [500,100,50,10,5,1]

change = 1000 - int(input())
n = 0

for c in coin:
    n += change // c
    change %= c

print(n)

