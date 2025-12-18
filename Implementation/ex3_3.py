
n = 8
location = input()

col = ord(location[0])-ord('a') + 1
row = int(location[1])

cnt = 0

#위위오

#위위왼

if row - 2 > 0:
    if col + 1 <= 8:
        cnt += 1
    if col - 1 > 0:
        cnt += 1

#아아오

#아아왼

if row + 2 <= 8:
    if col + 1 <= 8:
        cnt += 1
    if col - 1 > 0:
        cnt += 1

#왼왼위

#왼왼아

if col - 2 > 0:
    if row + 1 <= 8:
        cnt += 1
    if row - 1 > 0:
        cnt += 1

#오오위

#오오아

if col + 2 <= 8:
    if row + 1 <= 8:
        cnt += 1
    if row - 1 > 0:
        cnt += 1

print(cnt)