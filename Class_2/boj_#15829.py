'''

5
abcde

4739715

'''

N = int(input())

a = input()

result = 0

for i in range(N):
    result += (ord(a[i]) - 96) * (31 ** i)

print(result)
