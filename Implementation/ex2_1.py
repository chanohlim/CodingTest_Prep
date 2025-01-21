import time

h = int(input())
cnt = 0

s = time.time()

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1


print(cnt)
print(format(time.time() - s, 'f'))