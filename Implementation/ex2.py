import time

n = int(input())
cnt_h = 0
cnt = 0

s = time.time()
for i in range(n+1):
    if '3' in str(i):
        cnt_h += 1

for i in range(60):
    if '3' in str(i):
        cnt += 1

in_sec = cnt*(60-cnt)
in_min = cnt*60

print((in_sec + in_min)*n + cnt_h*60*60)
print(format(time.time() - s, 'f'))